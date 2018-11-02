# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
# is the index of a leaf with a possibly out-of-order value passed in 'new' object.  Restore the
# heap invariant.


def decrease_key(heap, startpos, pos, new):
    if new.cost < heap[pos].cost:
        while pos > startpos:  # follow the path to the root, moving parents down until finding a place wher newitem fits
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if new < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = new
        return True
    return False