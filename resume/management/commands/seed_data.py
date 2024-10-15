from django.core.management.base import BaseCommand
from resume.models import Resume, Skill, TypeSkill, WorkExperience, Education,  Project, Certification, Reference, CustomUser, WorkExperienceDescription, WorkExperienceTool
from datetime import date

class Command(BaseCommand):
    help = 'Insert sample resume data into the database'

    def handle(self, *args, **kwargs):

        json_data ={
                "name": "Your Name",
                "title": "DHIS2 Consultant | Software Developer",
                "experience": [
                    {
                    "role": "DHIS 2 Consultant",
                    "company": "The World Bank",
                    "type": "Part-time",
                    "date": {
                        "start": "2022-07-01",
                        "end": "2024-01-01"
                    },
                    "location": "Guinea",
                    "details": [
                        "Training and mentoring of senior staff at the Ministry of Health on effective management and maintenance of all applications.",
                        "Correction of issues found in the new DHIS2 instance and transfer of high-quality data from the archive instance to the new DHIS2 instance.",
                        "Leading the revision of data collection tools at the Ministry of Health and initiating data entry for Health Posts in DHIS2."
                    ],
                    "skills": [
                        "React.js", "Docker", "Spring boot", "PostgreSQL", "DHIS2", "Go", "Ubuntu"
                    ]
                    },
                    {
                    "role": "LLIN Campaign Digitization Consultant",
                    "company": "Catholic Relief Services",
                    "type": "Self-employed",
                    "date": {
                        "start": "2022-02-01",
                        "end": "2022-06-01"
                    },
                    "location": "Guinea",
                    "details": [
                        "Supported the digitization of the long-lasting insecticidal nets (LLIN) distribution campaign using DHIS2-based tools.",
                        "Installed and administered the campaign server and trained personnel responsible for counting and distributing LLINs.",
                        "Provided continuous technical support to ensure proper functioning of digital tools and accuracy of data collected throughout the campaign."
                    ],
                    "skills": [
                        "Android Development", "Docker", "PostgreSQL", "DHIS2", "Lxc", "Ubuntu"
                    ]
                    },
                    {
                    "role": "Health Information System Consultant",
                    "company": "The World Bank",
                    "type": "Full-time",
                    "date": {
                        "start": "2021-04-01",
                        "end": "2021-10-01"
                    },
                    "location": "Guinea",
                    "details": [
                        "Implemented the new DHIS2 platform for the Ministry of Health, including server installation, creation of DHIS2 instances, and development of data collection tools.",
                        "Created indicators and dashboards, and trained users to ensure effective use of the platform."
                    ],
                    "skills": [
                        "Node.js", "React.js", "Docker", "Spring boot", "PostgreSQL", "DHIS2", "Go", "Linux", "Ubuntu"
                    ]
                    },
                    {
                    "role": "Lead Data Manager",
                    "company": "African Field Epidemiology Network (AFENET)",
                    "type": "Full-time",
                    "date": {
                        "start": "2020-02-01",
                        "end": "2021-04-01"
                    },
                    "location": "Conakry, Guinea",
                    "details": [
                        "Implemented the COVID-19 data management system for the Ministry of Health of Guinea, including contact tracing for confirmed cases and development of key surveillance indicators and dashboards.",
                        "Designed and developed the COVID-19 vaccination certificate production system.",
                        "Developed a system for delivering COVID-19 test results via SMS."
                    ],
                    "skills": [
                        "Node.js", "React.js", "Docker", "Spring boot", "PostgreSQL", "DHIS2", "Java", "Ubuntu"
                    ]
                    },
                    {
                    "role": "Lead Data Manager",
                    "company": "RTI International",
                    "type": "Full-time",
                    "date": {
                        "start": "2017-11-01",
                        "end": "2020-01-01"
                    },
                    "location": "Conakry, Guinea",
                    "details": [
                        "Implemented the Health Information System of Guinea based on DHIS2 for the Global Health Security Agenda project in collaboration with the CDC.",
                        "Configured data collection tools for routine data and epidemiological surveillance for malaria, HIV/AIDS, tuberculosis, and maternal death data.",
                        "Trained health workers on the use of DHIS2 at all levels of the health pyramid."
                    ],
                    "skills": [
                        "Node.js", "Android Development", "Git", "JHipster", "React.js", "Docker", "Spring boot", "PostgreSQL", "DHIS2", "Ubuntu"
                    ]
                    },
                    {
                    "role": "Senior Software Developer",
                    "company": "ETI SA",
                    "type": "Full-time",
                    "date": {
                        "start": "2012-02-01",
                        "end": "2017-10-01"
                    },
                    "location": "Guinea",
                    "details": [
                        "Participated in the design and development of identification and security systems based on multi-biometric solutions (fingerprint, facial, iris).",
                        "Developed fingerprint, facial, and iris recognition solutions, and automatic and manual deduplication systems.",
                        "Developed secure documents including biometric passports, identity cards, and driver's licenses."
                    ],
                    "skills": [
                        "Git", "Spring boot", "Oracle SQL Developer", "PostgreSQL", "MySQL", "Java", "C#"
                    ]
                    }
                ],
                "education": [
                    {
                    "degree": "English as a Second Language",
                    "institution": "University of Boston",
                    "date": {
                        "start": "2024-01-01"
                    }
                    },
                    {
                    "degree": "Academy DHIS 2 Android Implementation",
                    "institution": "University Of Oslo / HISP Africa",
                    "date": {
                        "start": "2018-02-01"
                    }
                    },
                    {
                    "degree": "Training on DHIS2 Mobile Eco System",
                    "institution": "University of Oslo",
                    "date": {
                        "start": "2018-02-01"
                    }
                    },
                    {
                    "degree": "Oracle Application Express",
                    "institution": "ETI S.A",
                    "date": {
                        "start": "2017-05-01"
                    }
                    },
                    {
                    "degree": "Agile Scrum",
                    "institution": "ETI S.A",
                    "date": {
                        "start": "2016-12-01"
                    }
                    },
                    {
                    "degree": "Android Development",
                    "institution": "Mistra / Paris",
                    "date": {
                        "start": "2015-12-01"
                    }
                    },
                    {
                    "degree": "Spring Framework",
                    "institution": "Mistra / Paris",
                    "date": {
                        "start": "2015-12-01"
                    }
                    },
                    {
                    "degree": "Quality Management Systems",
                    "institution": "ETI S.A",
                    "date": {
                        "start": "2014-01-01"
                    },
                    "description": "ISO-9001 standards version 2008"
                    },
                    {
                    "degree": "Computer Science",
                    "institution": "Gamal Abdel Nasser University of Conakry",
                    "date": {
                        "start": "2007-10-01",
                        "end": "2010-04-01"
                    }
                    }
                ],
                "technicalSkills": [
                    "DHIS2", "React.js", "Docker", "Spring Boot", "PostgreSQL", "Node.js", "Go", "Ubuntu", "Android Development", "JHipster", "Java", "Linux"
                ],
                "softSkills": [
                    "Team Leadership", "Problem Solving", "Adaptability", "Communication", "Time Management", "Mentoring", "Training"
                ]
                }
        # Get or create a user
        user, created = CustomUser.objects.get_or_create(
            username='moussa',
            defaults={
                'email': 'moussa@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'phone_number':'425-526-872',
                'github': '/didate',
                'linkedin': '/in/rsdiallo',
                'website': 'mldiallo.com'
            }
        )

        if created:
            user.set_password("?Fjs!4Q&m8HC3cLD")
            user.save()
        
        # Create Resume object
        resume = Resume.objects.create(
            user=user,
            title=json_data['title'],
            summary= "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni perferendis exercitationem saepe eum culpa quaerat, iusto sequi optio nulla cupiditate laudantium qui nemo accusantium consectetur ullam, corrupti voluptatibus tempora tenetur."
        )

        backend_type_skill = TypeSkill.objects.create(
            resume = resume,
            name = "Backend"
        )

        soft_type_skill = TypeSkill.objects.create(
            resume = resume,
            name = "Soft"
        )

        for exp in json_data['experience']:
            # Use the start and end dates from the nested date object
            start_date = exp['date'].get('start')
            end_date = exp['date'].get('end')  # This can be None if not provided

            # Create WorkExperience object
            work_experience = WorkExperience.objects.create(
                resume=resume,
                company=exp['company'],
                job_title=exp['role'],
                start_date=start_date,
                end_date=end_date
            )

            # Create WorkExperienceDescription objects
            for detail in exp['details']:
                WorkExperienceDescription.objects.create(
                    work_experience=work_experience,
                    description=detail
                )

            # Create WorkExperienceTool objects
            for skill in exp['skills']:
                WorkExperienceTool.objects.create(
                    work_experience=work_experience,
                    name=skill
                )

        # Create Education objects
        for edu in json_data['education']:
            # Use the start and end dates from the nested date object (if you have similar structure for education)
            start_date = edu['date'].get('start') if 'date' in edu else None
            end_date = edu['date'].get('end') if 'date' in edu else None  # This can be None if not provided

            # Create Education object
            Education.objects.create(
                resume=resume,
                school=edu['institution'],
                degree=edu['degree'],
                start_date=start_date,
                end_date=end_date
            )

        # Create TechSkill objects
        for tech_skill in json_data['technicalSkills']:
            Skill.objects.create(
                resume=resume,
                name=tech_skill,
                type_skill = backend_type_skill
            )

        # Create SoftSkill objects
        for soft_skill in json_data['softSkills']:
            Skill.objects.create(
                resume=resume,
                name=soft_skill,
                type_skill = soft_type_skill
            )

        # Projects
        Project.objects.create(
            resume=resume,
            title="Sales Data Analysis",
            description="Analyzed sales data for a retail company to identify purchasing trends and customer behavior. Provided actionable insights that led to a 15% increase in revenue.",
            start_date=date(2022, 1, 1),
            end_date=date(2022, 6, 1)
        )

        Project.objects.create(
            resume=resume,
            title="Customer Segmentation",
            description="Used clustering algorithms in Python to segment customer data and improve targeted marketing efforts, resulting in a 25% increase in customer retention.",
            start_date=date(2021, 2, 1),
            end_date=date(2021, 8, 1)
        )

        # Certifications
        Certification.objects.create(
            resume=resume,
            name="Certified Data Analyst (CDA)",
            authority="Data Science Council of America (DASCA)",
            date_earned=date(2021, 5, 1)
        )

        # References
        Reference.objects.create(
            resume=resume,
            name="Michael Brown",
            relationship="Former Supervisor",
            phone_number="555-987-6543",
            email="michael.brown@example.com",
            company="Data Insights LLC"
        )

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully.'))