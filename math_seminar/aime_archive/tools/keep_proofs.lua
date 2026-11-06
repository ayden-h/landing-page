-- Keep a short theorem statement and its proof together when the page permits.
-- Long proofs are allowed to break; this filter only groups modest blocks.
function Pandoc(doc)
  local out, pending, active = {}, {}, false
  local function flush(group)
    if #group == 0 then return end
    local count = 0
    for _, b in ipairs(group) do count = count + #pandoc.utils.stringify(b) end
    if count < 2300 then table.insert(out, pandoc.RawBlock('latex','\\begin{samepage}')) end
    for _, b in ipairs(group) do table.insert(out,b) end
    if count < 2300 then table.insert(out, pandoc.RawBlock('latex','\\end{samepage}')) end
  end
  for _,b in ipairs(doc.blocks) do
    local s=pandoc.utils.stringify(b)
    if not active and (s:match('^Theorem ') or s:match('^Lemma ') or s:match('^Proposition ') or s:match('^Corollary ') or s:match('^Derived proposition ')) then
      active=true;pending={b}
    elseif active then
      if b.t=='Header' then flush(pending);pending={};active=false;table.insert(out,b)
      else
        table.insert(pending,b)
        local done=false
        pandoc.walk_block(b,{Math=function(m) if m.text:match('\\square') then done=true end end})
        if done then flush(pending);pending={};active=false end
      end
    else table.insert(out,b) end
  end
  flush(pending)
  return pandoc.Pandoc(out,doc.meta)
end
