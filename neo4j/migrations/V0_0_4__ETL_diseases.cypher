// assert that edition is community
// assert that version is ge 4.4
CREATE (agent:`007`) RETURN agent;
UNWIND RANGE(1,6) AS i
WITH i CREATE (n:OtherAgents {idx: '00' + i})
RETURN n
;