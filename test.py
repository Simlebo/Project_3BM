from dB_3BM_Project import select_fabrication_step
from dB_3BM_Project import insert_fabrication_step

rows_step = select_fabrication_step("")
step_id = len(rows_step) + 1
machine_id = float(22)
time = float(444)
step_name = "hiehie"
fabrication_step = 1
product_id = 3


insert_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name)