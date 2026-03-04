# ==========================================================
# Dataset: Online Course Platform Analytics
# ==========================================================

import pandas as pd
import plotly.express as px


data = pd.DataFrame({
    "Course": [
        "Python Basics", "Data Analysis", "Machine Learning",
        "Web Development", "SQL Fundamentals", "Deep Learning"
    ],
    
    "Enrollments": [1200, 950, 800, 1100, 1000, 650],
    
    "Completion Rate": [72, 68, 60, 74, 70, 55],
    
    "Rating": [4.6, 4.5, 4.7, 4.4, 4.3, 4.6],
    
    "Category": [
        "Programming", "Data Science", "AI",
        "Programming", "Database", "AI"
    ]
})

print(data)


# bar chart --- 

fig1 = px.bar(
    
    data_frame = data,
    
    x = "Course",
    
    y = "Enrollments",
    
    color =  "Category",
    
    title ="Course enrollments by category"
)

fig1.show()

# python basics has the highest ernrollments indicating
# strong demand for beginner programming courses.



# scatter chart

fig2 = px.scatter(
    
    data_frame = data,
    
    x = "Completion Rate",
    
    y = "Rating",
    
    color = "Category",
    
    hover_data = ["Course"],
    
    title = "Completion Rate vs Course Rating"
)

fig2.show()


# courses with higher completion rates tend to have slightly better ratings



# line chart

fig3 = px.line(
    
    data_frame = data,
    
    x = "Course",
    
    y = "Completion Rate",
    
    markers = True,
    
    title = "Course completion rate by course"
)

fig3.show()



# web dev shows the highest completion rate, 
# indicating students are highly engaged with this course


fig1.write_html(
    
    "course_dashboard.html"
)

