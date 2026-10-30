--[[
filtro_apa.lua — se ejecuta ANTES de --citeproc.
* Asigna estilos de Word (custom-style) a los entornos generados por
  tesis_a_docx.py (leyendas, notas, figuras, carátula, índices...).
* \textcolor{pendientecolor}{...} -> estilo de carácter «Pendiente» (rojo).
* El entorno «bibliografiaapa» se convierte en el Div #refs donde citeproc
  coloca la lista de referencias.
]]

local estilos_div = {
  apaleyenda = 'Caption',
  apanota = 'Nota APA',
  apafigura = 'Figura APA',
  caratula = 'Caratula',
  listaetiquetada = 'Lista etiquetada',
  tituloindice = 'TOC Heading',
  indice1 = 'toc 1',
  indice2 = 'toc 2',
  indice3 = 'toc 3',
  indicefig = 'table of figures',
  recuadro = 'Recuadro',
}

function Div(el)
  for _, c in ipairs(el.classes) do
    if c == 'bibliografiaapa' then
      return pandoc.Div({}, pandoc.Attr('refs'))
    end
    local estilo = estilos_div[c]
    if estilo then
      el.attributes['custom-style'] = estilo
      return el
    end
  end
end

function Span(el)
  local s = el.attributes['style']
  if s and s:match('pendientecolor') then
    el.attributes['style'] = nil
    el.attributes['custom-style'] = 'Pendiente'
    return el
  end
end
