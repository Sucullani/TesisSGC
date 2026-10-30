# -*- coding: utf-8 -*-
"""LibreOffice (opcional): números de página del índice y PDF de verificación.

Los índices del .docx (general, de tablas y de figuras) usan campos PAGEREF.
Word los actualiza al abrir el documento (pregunta «¿Actualizar los campos?»).
Para que el .docx muestre números aunque no se actualicen, se abre una vez con
LibreOffice (UNO), se leen las páginas que calcula para cada marcador y se
escriben como valor guardado de los campos.  También puede exportar un PDF.
"""

import os
import re
import shutil
import socket
import subprocess
import tempfile
import time
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


def _puerto_libre():
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    p = s.getsockname()[1]
    s.close()
    return p


def abrir_con_libreoffice(ruta_docx, ruta_pdf=None, avisos=None, timeout=300):
    """Devuelve {marcador: página} y, si se pide, exporta el PDF."""
    avisos = avisos if avisos is not None else []
    try:
        import uno
        from com.sun.star.beans import PropertyValue
    except ImportError:
        avisos.append('No está disponible el puente UNO de LibreOffice; no se calculan las páginas del índice.')
        return {}
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        avisos.append('No se encontró LibreOffice (soffice).')
        return {}

    def pv(nombre, valor):
        p = PropertyValue()
        p.Name, p.Value = nombre, valor
        return p
    perfil = tempfile.mkdtemp(prefix='lo_perfil_')
    puerto = _puerto_libre()
    proc = subprocess.Popen([soffice, '--headless', '--invisible', '--nologo', '--norestore', '--nodefault',
                             '-env:UserInstallation=%s' % Path(perfil).as_uri(),
                             '--accept=socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext' % puerto],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    paginas = {}
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
        ctx = None
        t0 = time.time()
        while time.time() - t0 < 60:
            try:
                ctx = resolver.resolve('uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext' % puerto)
                break
            except Exception:
                time.sleep(0.5)
        if ctx is None:
            avisos.append('LibreOffice no respondió.')
            return {}
        escritorio = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
        doc = escritorio.loadComponentFromURL(Path(ruta_docx).resolve().as_uri(), '_blank', 0,
                                              (pv('Hidden', True), pv('UpdateDocMode', 3)))
        campos = doc.getTextFields()
        campos.refresh()
        try:
            doc.getDocumentIndexes()
        except Exception:
            pass
        enum = campos.createEnumeration()
        while enum.hasMoreElements():
            f = enum.nextElement()
            try:
                if f.supportsService('com.sun.star.text.TextField.GetReference'):
                    nombre = f.SourceName
                    valor = f.getPresentation(False)
                    if nombre and valor:
                        paginas[nombre] = valor
            except Exception:
                continue
        if ruta_pdf:
            doc.storeToURL(Path(ruta_pdf).resolve().as_uri(), (pv('FilterName', 'writer_pdf_Export'),))
        doc.close(True)
    except Exception as e:
        avisos.append('Error al usar LibreOffice: %s' % e)
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=20)
        except Exception:
            proc.kill()
        shutil.rmtree(perfil, ignore_errors=True)
    return paginas


def escribir_paginas(ruta_docx, paginas):
    """Pone el número de página calculado como valor guardado de cada PAGEREF."""
    doc = Document(str(ruta_docx))
    cambiados = 0
    # Formato de numeración de la sección de cada marcador (romanos en las páginas preliminares)
    body = doc.element.body
    bloques = list(body)
    fines = []
    for i, e in enumerate(bloques):
        sp = e if e.tag == qn('w:sectPr') else (e.find('.//' + qn('w:sectPr')) if e.tag == qn('w:p') else None)
        if sp is not None:
            pn = sp.find(qn('w:pgNumType'))
            fines.append((i, pn.get(qn('w:fmt')) if pn is not None else 'decimal'))
    formato = {}
    for i, e in enumerate(bloques):
        for b in ([e] if e.tag == qn('w:bookmarkStart') else e.iter(qn('w:bookmarkStart'))):
            fmt = next((f for j, f in fines if j >= i), 'decimal')
            formato[b.get(qn('w:name'))] = fmt

    def romano(n):
        vals = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'), (50, 'l'),
                (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
        r = ''
        for v, t in vals:
            while n >= v:
                r, n = r + t, n - v
        return r
    paginas = dict(paginas)
    for nombre, valor in list(paginas.items()):
        if formato.get(nombre) == 'lowerRoman' and str(valor).isdigit():
            paginas[nombre] = romano(int(valor))
    for p in doc.element.body.iter(qn('w:p')):
        runs = list(p.iter(qn('w:r')))
        destino = None
        estado = None
        for r in runs:
            fc = r.find(qn('w:fldChar'))
            it = r.find(qn('w:instrText'))
            if fc is not None:
                tipo = fc.get(qn('w:fldCharType'))
                if tipo == 'begin':
                    estado, destino = 'instr', None
                elif tipo == 'separate':
                    estado = 'valor'
                elif tipo == 'end':
                    estado = None
                continue
            if it is not None and estado == 'instr':
                m = re.match(r'\s*PAGEREF\s+(\S+)', it.text or '')
                if m:
                    destino = m.group(1)
                continue
            if estado == 'valor' and destino and destino in paginas:
                t = r.find(qn('w:t'))
                if t is not None:
                    t.text = paginas[destino]
                    cambiados += 1
                    destino = None
    doc.save(str(ruta_docx))
    return cambiados
