-- Textual review notes sometimes use Unicode symbols outside math delimiters.
-- Render these with the mathematics font rather than silently dropping glyphs.
local symbols = {
 ['≤']='\\le', ['≥']='\\ge', ['≠']='\\ne', ['≡']='\\equiv',
 ['∈']='\\in', ['∪']='\\cup', ['∩']='\\cap', ['⧵']='\\smallsetminus',
 ['∠']='\\angle', ['∥']='\\parallel', ['⊥']='\\perp', ['≈']='\\approx',
 ['→']='\\to', ['↦']='\\mapsto', ['⋯']='\\cdots', ['∏']='\\prod',
 ['√']='\\sqrt{\\vphantom{0}}', ['−']='-', ['±']='\\pm', ['×']='\\times',
 ['α']='\\alpha', ['β']='\\beta', ['γ']='\\gamma', ['θ']='\\theta',
 ['λ']='\\lambda', ['π']='\\pi', ['Σ']='\\Sigma', ['τ']='\\tau',
 ['φ']='\\phi', ['ω']='\\omega', ['′']='{}^{\\prime}', ['″']='{}^{\\prime\\prime}',
 ['⁰']='{}^0', ['¹']='{}^1', ['²']='{}^2', ['³']='{}^3', ['⁴']='{}^4',
 ['⁵']='{}^5', ['⁶']='{}^6', ['⁷']='{}^7', ['⁸']='{}^8', ['⁹']='{}^9',
 ['ⁿ']='{}^n', ['ʲ']='{}^j', ['ᵉ']='{}^e', ['⁻']='{}^{-}', ['⁺']='{}^{+}',
 ['₀']='{}_0', ['₁']='{}_1', ['₂']='{}_2', ['₃']='{}_3', ['₄']='{}_4',
 ['₅']='{}_5', ['₆']='{}_6', ['₇']='{}_7', ['₈']='{}_8', ['₉']='{}_9',
 ['ₙ']='{}_n', ['ₖ']='{}_k', ['₊']='{}_{+}', ['₋']='{}_{-}', ['₌']='{}_{=}',
 ['ᵢ']='{}_i', ['ⱼ']='{}_j', ['ₓ']='{}_x', ['ᵧ']='{}_y', ['ᵣ']='{}_r', ['ₚ']='{}_p',
 ['⅔']='\\frac{2}{3}'
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
