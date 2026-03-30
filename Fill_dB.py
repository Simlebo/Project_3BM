import dB_3BM_Project
from datetime import datetime

dB_3BM_Project.insert_users(1,'Philippe Fraiseuse 5 axis','philippe.fraiseuse@example.com')
dB_3BM_Project.insert_machine(1,1,12)
dB_3BM_Project.insert_product(1,0,0,'None')
dB_3BM_Project.insert_product(2,500,200,'Product A')
dB_3BM_Project.insert_fabrication_step(1,2,1,1,60,'Cutting')
dB_3BM_Project.insert_customer(1,1,'Edouard Dupont','BE16521316320')
dB_3BM_Project.insert_customer_order(1,1,datetime.now())
dB_3BM_Project.insert_order_details(1,1,2,5)

dB_3BM_Project.insert_users(2,'Alice Turner scie a ruban','alice.turner@example.com')
dB_3BM_Project.insert_machine(2,2,2)

dB_3BM_Project.insert_users(3,'Bob Tourneur','bob.tourneur@example.com')
dB_3BM_Project.insert_machine(3,3,5)

dB_3BM_Project.insert_users(4,'Charlie Martin metrologie','charlie.martin@example.com')
dB_3BM_Project.insert_machine(4,4,0)

dB_3BM_Project.insert_product(3,800,120,'Product B')
dB_3BM_Project.insert_fabrication_step(2,3,2,1,30,'Decoupage du brut')
dB_3BM_Project.insert_fabrication_step(3,3,1,2,45,'Surfaçage et perçage')
dB_3BM_Project.insert_fabrication_step(4,3,3,3,180,'Chariotage, débauchage et Finition')
dB_3BM_Project.insert_fabrication_step(5,3,4,4,60,'Contrôle qualité')