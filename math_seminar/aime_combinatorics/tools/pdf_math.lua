-- Textual review notes sometimes use Unicode symbols outside math delimiters.
-- Render these with the mathematics font rather than silently dropping glyphs.
local symbols = {['≤']='\\le', ['≥']='\\ge', ['≠']='\\ne', ['θ']='\\theta',
  ['∪']='\\cup', ['∩']='\\cap', ['₂']='{}_2', ['⁴']='{}^4', ['⧵']='\\smallsetminus'}
function Str(el)
  local out, pending = {}, ''
  for _,cp in utf8.codes(el.text) do
    local ch=utf8.char(cp)
    if symbols[ch] then
      if #pending>0 then table.insert(out,pandoc.Str(pending));pending='' end
      table.insert(out,pandoc.Math('InlineMath',symbols[ch]))
    else pending=pending..ch end
  end
  if #pending>0 then table.insert(out,pandoc.Str(pending)) end
  return out
end

-- Long inline inventories should wrap at commas instead of crossing margins.
function Math(el)
  if el.mathtype=='InlineMath' then
    el.text=el.text:gsub(',',',\\allowbreak ')
  end
  return el
end
