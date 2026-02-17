import csv

class student:
        def __init__(self,student_id,name,maths,phy,chem,bio):
                self.student_id = student_id
                self.name = name
                self.maths = int(maths)
                self.phy = int(phy)
                self.chem = int(chem)
                self.bio = int(bio)

        def avg(self):
                return (self.maths + self.phy + self.chem + self.bio)/4


def gen_report(inp_file,op_file):
        students=[]

        try:
                with open(inp_file,'r') as file:
                        rdr=csv.DictReader(file)
                        for row in rdr:
                                Student = student(row['StudentID'],
                                                  row['Name'],
                                                  row['Math'],
                                                  row['Physics'],
                                                  row['Chemistry'],
                                                  row['Biology'])
                                students.append(Student)

        except FileNotFoundError:
                print("Error: File not found")
                return

        total_studs=len(students)

        total_maths = sum(s.maths for s in students)
        total_phy   = sum(s.phy for s in students)
        total_chem  = sum(s.chem for s in students)
        total_bio   = sum(s.bio for s in students)

        maths_cls_avg = total_maths/total_studs
        phy_cls_avg  = total_phy/total_studs
        chem_cls_avg = total_chem/total_studs
        bio_cls_avg  = total_bio/total_studs

        all_sub_avg = (maths_cls_avg+phy_cls_avg+chem_cls_avg+bio_cls_avg)/4

        above_90_studs = [s for s in students if s.maths>90 or s.chem>90 or s.phy>90 or s.bio>90]

        top_3_studs = sorted(students, key=lambda s: s.avg(),reverse=True)[:3]

        high_maths = max(students, key=lambda s: s.maths)
        low_maths  = min(students, key=lambda s: s.maths)

        high_phy = max(students, key=lambda s: s.phy)
        low_phy  = min(students, key=lambda s: s.phy)

        high_chem = max(students, key=lambda s: s.chem)
        low_chem  = min(students, key=lambda s: s.chem)
        
        high_bio = max(students, key=lambda s: s.bio)
        low_bio  = min(students, key=lambda s: s.bio)

        with open(op_file, 'w') as report:

                report.write("------------ STUDENT REPORT -------------\n\n")

                report.write(f"Total Students : {total_studs}\n\n")

                report.write("Class Average:\n")
                report.write(f"Maths : {maths_cls_avg:.2f}\n")
                report.write(f"Physics : {phy_cls_avg:.2f}\n")
                report.write(f"Chemistry : {chem_cls_avg:.2f}\n")
                report.write(f"Biology : {bio_cls_avg:.2f}\n")
                report.write(f"Overall class average : {all_sub_avg:.2f}\n\n")

                report.write("Top 3 Students:\n")
                for s in top_3_studs:
                        report.write(f"{s.name} ({s.student_id}) - Avg : {s.avg():.2f}\n")

                report.write("\nstudents scoring above 90:\n")
                for s in above_90_studs:
                        report.write(f"{s.name} ({s.student_id})\n")

                report.write("\nSubject-wise Highest and Lowest:\n")
                report.write(f"Maths - High : {high_maths.name} ({high_maths.maths}), "
                             f"Low : {low_maths.name} ({low_maths.maths})\n")

                report.write(f"Physics - High : {high_phy.name} ({high_phy.phy}), "
                             f"Low : {low_phy.name} ({low_phy.phy})\n")

                report.write(f"Chemistry - High : {high_chem.name} ({high_chem.chem}), "
                             f"Low : {low_chem.name} ({low_chem.chem})\n")

                report.write(f"Biology - High : {high_bio.name} ({high_bio.bio}), "
                             f"Low : {low_bio.name} ({low_bio.bio})\n")

        print("Report generated successfully")

with open("students.csv","w") as f:
        f.write("StudentID,Name,Math,Physics,Chemistry,Biology\n")
        f.write("S001,Alice Johnson,85,90,88,92\n")
        f.write("S002,Bob Smith,78,82,75,80\n")
        f.write("S003,Carol White,92,88,95,90\n")
        f.write("S004,David Brown,70,68,72,75\n")

gen_report("students.csv","report.txt")

print("------------students.csv---------------")
with open("students.csv","r") as f:
        print(f.read())
                
print("--------------report.txt---------------")
with open("report.txt","r") as f:
        print(f.read())
