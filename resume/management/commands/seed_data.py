from django.core.management.base import BaseCommand
from resume.models import Resume, WorkExperience, Education, Skill, Project, Certification, Reference, CustomUser
from datetime import date

class Command(BaseCommand):
    help = 'Insert sample resume data into the database'

    def handle(self, *args, **kwargs):
        # Get or create a user
        user, created = CustomUser.objects.get_or_create(
            username='moussa',
            defaults={'email': 'moussa@example.com', 'first_name': 'John', 'last_name': 'Doe', 'phone_number':'425526872'}
        )
        if created:
            user.set_password('?Fjs!4Q&m8HC3cLD')
            user.save()

        # Create the Software Developer Resume
        software_developer_resume = Resume.objects.create(
            user=user,
            title="Software Developer Resume",
            summary="Highly skilled software developer with 5+ years of experience in building robust web applications. Proficient in modern JavaScript frameworks, backend development, and agile methodologies."
        )

        # Work Experience
        WorkExperience.objects.create(
            resume=software_developer_resume,
            company="TechCorp",
            job_title="Full Stack Developer",
            start_date=date(2020, 1, 1),
            end_date=date(2023, 1, 1),
            description="Developed and maintained web applications using React, Node.js, and PostgreSQL. Improved application performance and ensured a smooth deployment process using CI/CD pipelines."
        )

        WorkExperience.objects.create(
            resume=software_developer_resume,
            company="DevSolutions",
            job_title="Backend Developer",
            start_date=date(2017, 6, 1),
            end_date=date(2019, 12, 31),
            description="Designed and developed scalable APIs using Django and Flask. Managed database performance and optimized backend systems."
        )

        # Education
        Education.objects.create(
            resume=software_developer_resume,
            school="University of Technology",
            degree="Bachelor of Science",
            field_of_study="Computer Science",
            start_date=date(2013, 9, 1),
            end_date=date(2017, 6, 1)
        )

        # Skills (Technical and Soft)
        Skill.objects.create(resume=software_developer_resume, name="Python", skill_type="technical")
        Skill.objects.create(resume=software_developer_resume, name="JavaScript", skill_type="technical")
        Skill.objects.create(resume=software_developer_resume, name="React", skill_type="technical")
        Skill.objects.create(resume=software_developer_resume, name="Communication", skill_type="soft")
        Skill.objects.create(resume=software_developer_resume, name="Teamwork", skill_type="soft")

        # Projects
        Project.objects.create(
            resume=software_developer_resume,
            title="E-Commerce Platform",
            description="Developed an e-commerce platform for a major retailer using React and Node.js. Integrated payment gateways and enhanced user experience.",
            start_date=date(2021, 2, 1),
            end_date=date(2022, 6, 1)
        )

        Project.objects.create(
            resume=software_developer_resume,
            title="Real-Time Chat Application",
            description="Built a real-time chat application using WebSockets and Node.js, enabling users to communicate in real-time with minimal latency.",
            start_date=date(2020, 3, 1),
            end_date=date(2020, 6, 1)
        )

        # Certifications
        Certification.objects.create(
            resume=software_developer_resume,
            name="AWS Certified Developer – Associate",
            authority="Amazon Web Services",
            date_earned=date(2021, 10, 1)
        )

        # References
        Reference.objects.create(
            resume=software_developer_resume,
            name="John Doe",
            relationship="Former Manager",
            phone_number="555-123-4567",
            email="john.doe@example.com",
            company="TechCorp"
        )


        # Get or create a user
        user, created = CustomUser.objects.get_or_create(
            username='didate',
            defaults={'email': 'data.analyst@example.com', 'first_name': 'Alice', 'last_name': 'Smith', 'phone_number':'834526872'}
        )
        if created:
            user.set_password('?Fjs!4Q&m8HC3cLD')
            user.save()

        # Create the Data Analyst Resume
        data_analyst_resume = Resume.objects.create(
            user=user,
            title="Data Analyst Resume",
            summary="Experienced data analyst with a strong background in interpreting large datasets to drive actionable business insights. Proficient in SQL, Python, and data visualization tools."
        )

        # Work Experience
        WorkExperience.objects.create(
            resume=data_analyst_resume,
            company="Data Insights LLC",
            job_title="Data Analyst",
            start_date=date(2020, 5, 1),
            end_date=date(2023, 4, 1),
            description="Analyzed large datasets to provide insights into business performance. Developed and maintained dashboards using Tableau and Power BI. Improved data accuracy and reporting speed by 20%."
        )

        WorkExperience.objects.create(
            resume=data_analyst_resume,
            company="Market Research Inc.",
            job_title="Junior Data Analyst",
            start_date=date(2017, 9, 1),
            end_date=date(2020, 4, 30),
            description="Cleaned, processed, and analyzed survey data for various research projects. Assisted in building predictive models using Python and Excel."
        )

        # Education
        Education.objects.create(
            resume=data_analyst_resume,
            school="National University of Analytics",
            degree="Bachelor of Science",
            field_of_study="Data Science",
            start_date=date(2013, 9, 1),
            end_date=date(2017, 6, 1)
        )

        # Skills (Technical and Soft)
        Skill.objects.create(resume=data_analyst_resume, name="SQL", skill_type="technical")
        Skill.objects.create(resume=data_analyst_resume, name="Python", skill_type="technical")
        Skill.objects.create(resume=data_analyst_resume, name="Tableau", skill_type="technical")
        Skill.objects.create(resume=data_analyst_resume, name="Power BI", skill_type="technical")
        Skill.objects.create(resume=data_analyst_resume, name="Problem-solving", skill_type="soft")
        Skill.objects.create(resume=data_analyst_resume, name="Attention to Detail", skill_type="soft")

        # Projects
        Project.objects.create(
            resume=data_analyst_resume,
            title="Sales Data Analysis",
            description="Analyzed sales data for a retail company to identify purchasing trends and customer behavior. Provided actionable insights that led to a 15% increase in revenue.",
            start_date=date(2022, 1, 1),
            end_date=date(2022, 6, 1)
        )

        Project.objects.create(
            resume=data_analyst_resume,
            title="Customer Segmentation",
            description="Used clustering algorithms in Python to segment customer data and improve targeted marketing efforts, resulting in a 25% increase in customer retention.",
            start_date=date(2021, 2, 1),
            end_date=date(2021, 8, 1)
        )

        # Certifications
        Certification.objects.create(
            resume=data_analyst_resume,
            name="Certified Data Analyst (CDA)",
            authority="Data Science Council of America (DASCA)",
            date_earned=date(2021, 5, 1)
        )

        # References
        Reference.objects.create(
            resume=data_analyst_resume,
            name="Michael Brown",
            relationship="Former Supervisor",
            phone_number="555-987-6543",
            email="michael.brown@example.com",
            company="Data Insights LLC"
        )

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully.'))