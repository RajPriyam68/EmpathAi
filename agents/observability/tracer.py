import uuid, time
def start_trace(name='trace'):
    tid = str(uuid.uuid4())
    print(f'[TRACE START] {tid} {name}')
    return tid
def end_trace(tid):
    print(f'[TRACE END] {tid}')
