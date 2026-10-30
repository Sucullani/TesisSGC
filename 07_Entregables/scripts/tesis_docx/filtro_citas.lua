--[[
filtro_citas.lua — se ejecuta DESPUÉS de --citeproc.
Abreviaturas de autores corporativos según APA 7 (como biblatex-apa con el
campo shortauthor):
  primera cita entre paréntesis:  (Organización Internacional de Normalización [ISO], 2026)
  primera cita narrativa:         Organización Internacional de Normalización (ISO, 2026)
  citas siguientes:               (ISO, 2026)  /  ISO (2026)
Las abreviaturas llegan en el metadato «abreviaturas-autores» (nombre: sigla).
]]

local abrev = {}
local vistos = {}

local function reemplazar(texto, buscado, nuevo, max)
  local res, n, ini = {}, 0, 1
  while true do
    local i, j = string.find(texto, buscado, ini, true)
    if not i or (max and n >= max) then break end
    table.insert(res, string.sub(texto, ini, i - 1))
    table.insert(res, nuevo)
    ini = j + 1
    n = n + 1
  end
  table.insert(res, string.sub(texto, ini))
  return table.concat(res), n
end

local function solo_texto(inlines)
  for _, el in ipairs(inlines) do
    local t = el.t
    if t ~= 'Str' and t ~= 'Space' and t ~= 'SoftBreak' then
      return false
    end
  end
  return true
end

local function procesar(el)
  if not solo_texto(el.content) then return nil end
  local texto = pandoc.utils.stringify(el.content)
  local narrativa = el.citations[1] and el.citations[1].mode == 'AuthorInText'
  local cambiado = false
  -- nombres más largos primero (por si uno contiene a otro)
  local nombres = {}
  for nombre, _ in pairs(abrev) do table.insert(nombres, nombre) end
  table.sort(nombres, function(a, b) return #a > #b end)
  for _, nombre in ipairs(nombres) do
    local sigla = abrev[nombre]
    if string.find(texto, nombre, 1, true) then
      if not vistos[nombre] then
        if narrativa then
          local t2, n = reemplazar(texto, nombre .. ' (', nombre .. ' (' .. sigla .. ', ', 1)
          if n == 0 then t2 = reemplazar(texto, nombre, nombre .. ' [' .. sigla .. ']', 1) end
          texto = t2
        else
          texto = reemplazar(texto, nombre, nombre .. ' [' .. sigla .. ']', 1)
        end
        -- otras apariciones en la misma cita
        local partes = {}
        local primero = true
        texto = texto:gsub(nombre:gsub('%p', '%%%0') .. '(%s?%[?)', function(sig)
          if primero then primero = false; return nombre .. sig end
          return sigla .. sig
        end)
        vistos[nombre] = true
      else
        texto = reemplazar(texto, nombre, sigla)
      end
      cambiado = true
    end
  end
  if cambiado then
    el.content = { pandoc.Str(texto) }
    return el
  end
end

function Pandoc(doc)
  local m = doc.meta['abreviaturas-autores']
  if m then
    for k, v in pairs(m) do abrev[k] = pandoc.utils.stringify(v) end
  end
  if next(abrev) == nil then return nil end
  return doc:walk({ Cite = procesar })
end
