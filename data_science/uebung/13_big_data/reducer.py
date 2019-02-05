import sys

current_id = None
current_count = 0
id = None


for line in sys.stdin:
    
    line = line.strip()

    
    id, count = line.split('\t', 1)

    count = float(count)

    if current_id == id:
        current_count += count
    else:
        if current_id:
            print('%s\t%s' % (current_id, current_count))
        current_count = count
        current_id = id


if current_id == id:
    print('%s\t%s' % (current_id, current_count))
