from image_processing.utils import get_center, merge_bounding_boxes

def cluster_date_of_expire(bboxes, horizontal_threshold=100):
    horizontally_sorted = sorted(bboxes, key=lambda b: (b[0], b[1]))
    date_of_expire_cluster = []

    for i, box in enumerate(horizontally_sorted):
        if not date_of_expire_cluster:
            date_of_expire_cluster.append(box)
            continue

        x_min = box[0]
        last_x_min = date_of_expire_cluster[-1][0]

        if abs(x_min - last_x_min) > horizontal_threshold:
            return date_of_expire_cluster, horizontally_sorted[i:]
        
        date_of_expire_cluster.append(box)
    
    return date_of_expire_cluster, []

def cluster_words(bboxes, vertical_threshold=30):
    vertically_sorted = sorted(bboxes, key=lambda b: (b[1], b[0]))
    word_clusters = []
    current_cluster = []

    for box in vertically_sorted:
        if not current_cluster:
            current_cluster.append(box)
            continue

        cluster_box = merge_bounding_boxes(current_cluster)
        vertical_distance = abs(get_center(box)[1] - get_center(cluster_box)[1])

        if vertical_distance < vertical_threshold:
            current_cluster.append(box)
        else:
            word_clusters.append(current_cluster)
            current_cluster = [box]
            
    if current_cluster:
        word_clusters.append(current_cluster)
    
    return word_clusters

def merge_bboxes(bboxes):
    date_of_expire_cluster, remainer = cluster_date_of_expire(bboxes)
    remainer_cluster = cluster_words(remainer)
    
    remainer_cluster.append(date_of_expire_cluster)
            
    return [merge_bounding_boxes(cluster) for cluster in remainer_cluster]