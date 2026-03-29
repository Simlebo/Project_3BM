from dB_3BM_Project import select_fabrication_step_number
from dB_3BM_Project import select_fabrication_step
g=select_fabrication_step("step_id = (SELECT MAX(step_id) FROM fabrication_step)")
f = float([x[0] for x in g][0])
print(f)

#print(select_fabrication_step_number())
