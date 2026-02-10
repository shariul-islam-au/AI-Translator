import csv
import os

bangla_sms_file = os.path.join(os.path.dirname(__file__), "bangla_sms.txt")

def read_sms_range(start: int, end: int) -> str:
    """
    Reads bangla_sms_file using csv.reader and returns a CSV string
    with header and rows from start to end (1-based, inclusive).
    """
    with open(bangla_sms_file, "r", encoding="utf-8", newline='') as f:
        reader = list(csv.reader(f))
    
    data_rows = reader[:]
    
    # Slice rows: start and end are 1-based indices, convert to zero-based for list
    selected_rows = data_rows[start+1:end+1]
    
    # Convert back to CSV string
    from io import StringIO
    output = StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    
    writer.writerows(selected_rows)
    
    return output.getvalue().strip()
read_sms_range(701, 750)