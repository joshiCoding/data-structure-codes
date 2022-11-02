def find_augmented_path(v):
    bfs.start_from_vertex(v)
    
    while bfs.has_unexplored_vertices():
        bfs.add_verticies_not_in_matching()

        # check for blossom
        if bfs.found_blossom():
            bfs.contract_blossom()
            find_augmented_path(v)
            bfs.lift_blossom()

        if bfs.found_augmented_path():
            return bfs.augmented_path()
        
        bfs.add_verticies_in_matching()
    
    return()

def improve_matching(G):
    for v in exposed_vertices(G):
        path = find_augmented_path(v)
        if path != []:
            switch_augmented_path(path)
            return True
    return False

while True:
    if not improve_matching(G):
        break
