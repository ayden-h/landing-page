-- Textual review notes sometimes use Unicode symbols outside math delimiters.
-- Render these with the mathematics font rather than silently dropping glyphs.
local symbols = {
  ['≤']='\\le',
  ['≥']='\\ge',
  ['≠']='\\ne',
  ['≡']='\\equiv',
  ['θ']='\\theta',
  ['φ']='\\varphi',
  ['∪']='\\cup',
  ['∩']='\\cap',
  ['⧵']='\\smallsetminus',
  ['₀']='{}_0',
  ['₁']='{}_1',
  ['₂']='{}_2',
  ['₃']='{}_3',
  ['₄']='{}_4',
  ['₅']='{}_5',
  ['₆']='{}_6',
  ['₇']='{}_7',
  ['₈']='{}_8',
  ['₉']='{}_9',
  ['⁰']='{}^{0}',
  ['¹']='{}^{1}',
  ['²']='{}^{2}',
  ['³']='{}^{3}',
  ['⁴']='{}^{4}',
  ['⁵']='{}^{5}',
  ['⁶']='{}^{6}',
  ['⁷']='{}^{7}',
  ['⁸']='{}^{8}',
  ['⁹']='{}^{9}',
  ['⁻']='{}^{-}',
}
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
