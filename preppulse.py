# PrepPulse AI - Simple Interview Readiness Score Prototype
# Python Console Version

print("========== PrepPulse AI ==========")

name = input("Enter your name: ")
role = input("Preferred Role: ")

print("\nRate yourself from 1 to 10")

technical = int(input("Technical Skills: "))
resume = int(input("Resume Quality: "))
communication = int(input("Communication Skills: "))
portfolio = int(input("Portfolio/GitHub: "))

# Weighted Score Calculation
final_score = (
    technical * 4 +
    resume * 2.5 +
    communication * 2 +
    portfolio * 1.5
)

# Readiness Level
if final_score < 40:
    level = "Beginner"
elif final_score < 70:
    level = "Intermediate"
elif final_score < 86:
    level = "Job Ready"
else:
    level = "Interview Pro"

print("\n========== RESULT ==========")
print("Candidate:", name)
print("Role:", role)
print("Interview Readiness Score:", final_score, "/100")
print("Level:", level)

print("\n========== FEEDBACK ==========")

if technical < 7:
    print("- Improve DSA, DBMS, OOPs and coding practice.")

if resume < 7:
    print("- Add projects, achievements and ATS keywords in resume.")

if communication < 7:
    print("- Practice speaking confidently and improve grammar.")

if portfolio < 7:
    print("- Upload more projects to GitHub and add README files.")

if (
    technical >= 7 and
    resume >= 7 and
    communication >= 7 and
    portfolio >= 7
):
    print("- Excellent profile! Keep practicing mock interviews.")

print("\nThank you for using PrepPulse AI 🚀")
