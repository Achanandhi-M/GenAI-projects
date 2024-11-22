import pandas as pd

# Sample data for students
data = {
    "Name": ["John Doe", "Jane Smith", "Rahul Kumar", "Priya Rani", "Arun Kumar", "Anjali Sharma", "Vijay Raj", "Neha Mehta", "Suresh Babu", "Priyanka Rao", 
             "Gokul Venkatesh", "Ananya Gupta", "Deepak Kumar", "Ramesh Reddy", "Tanvi Verma", "Aravind Nair", "Sangeeta Sharma", "Harish Kumar", "Bhavya Nair", "Rohit Jain"],
    "Marks": [88, 92, 80, 85, 78, 90, 95, 88, 75, 91, 82, 86, 89, 81, 92, 77, 90, 74, 88, 93],
    "Year": [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 2, 1, 3],
    "Area of Interest": ["Computer Science", "Electronics", "Mechanical Engineering", "Civil Engineering", "Data Science", "Electrical Engineering", "Artificial Intelligence", 
                         "Software Engineering", "Mechanical Engineering", "Biomedical Engineering", "Electrical Engineering", "Computer Science", "Civil Engineering", 
                         "Software Engineering", "Artificial Intelligence", "Data Science", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Software Engineering"],
    "Email": ["john.doe@email.com", "jane.smith@email.com", "rahul.kumar@email.com", "priya.rani@email.com", "arun.kumar@email.com", "anjali.sharma@email.com", 
              "vijay.raj@email.com", "neha.mehta@email.com", "suresh.babu@email.com", "priyanka.rao@email.com", "gokul.venkatesh@email.com", "ananya.gupta@email.com", 
              "deepak.kumar@email.com", "ramesh.reddy@email.com", "tanvi.verma@email.com", "aravind.nair@email.com", "sangeeta.sharma@email.com", "harish.kumar@email.com", 
              "bhavya.nair@email.com", "rohit.jain@email.com"],
    "Contact Number": ["+91 9876543210", "+91 9876543211", "+91 9876543212", "+91 9876543213", "+91 9876543214", "+91 9876543215", "+91 9876543216", 
                       "+91 9876543217", "+91 9876543218", "+91 9876543219", "+91 9876543220", "+91 9876543221", "+91 9876543222", "+91 9876543223", 
                       "+91 9876543224", "+91 9876543225", "+91 9876543226", "+91 9876543227", "+91 9876543228", "+91 9876543229"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Male", 
               "Female", "Male", "Female", "Male"],
    "College Name": ["ABC Engineering", "XYZ College", "SSC Engineering College", "Government Arts College", "XYZ College", "ABC Engineering", "Shri Punganur Engineering College", 
                     "SSC Engineering College", "SSPM Engineering College", "XYZ College", "ABC Engineering", "XYZ College", "SSC Engineering College", "Government Arts College", 
                     "Shri Punganur Engineering College", "XYZ College", "ABC Engineering", "SSPM Engineering College", "XYZ College", "Shri Punganur Engineering College"],
    "Address": ["Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", 
                "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", 
                "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu", 
                "Cuddalore, Tamil Nadu", "Cuddalore, Tamil Nadu"]
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_path = "/home/acha/student_details.xlsx"
df.to_excel(file_path, index=False)
