// assert that edition is community
// assert that version is ge 4.4
MATCH (agent:`007`) 
DETACH DELETE agent;
MATCH (n:OtherAgents)
DETACH DELETE n;