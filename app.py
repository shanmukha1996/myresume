from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

@app.route('/')
def index():
    portfolio_data = {
        'personal': {
            'name': 'Shanmukha Sai Ram Pavan Parvathina',
            'initials': 'SP',
            'title': 'Technical Specialist & OpenShift/Kubernetes SME',
            'subtitle': 'AI Engineer | Cloud Solutions Architect | Certified Kubernetes Expert',
            'location': 'Dublin, Ireland',
            'email': 'psspavan96@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/pavan-pss/',
            'medium': 'https://psspavan96.medium.com/'
        },
        
        'summary': 'Certified Technical Specialist and hands-on AI Engineer/OpenShift SME with proven expertise in managing and supporting large-scale Kubernetes and OpenShift multi-cluster environments. Skilled in cluster administration, automated deployments, patch management, and RBAC/AD integration, ensuring secure and efficient operations. Strong track record in supporting enterprise-grade containerized environments and implementing end-to-end CI/CD pipelines. Experience with Model Serving with OpenShift AI and Agentic development.',
        
        'highlights': [
            {
                'icon': 'fa-cube',
                'title': 'Technical Leadership',
                'description': 'Leading enterprise-scale cloud solutions and guiding engineering decisions as a subject-matter expert on OpenShift and Kubernetes architectures.'
            },
            {
                'icon': 'fa-cloud',
                'title': 'Cloud & Container Expertise',
                'description': 'Expert in Kubernetes/OpenShift multi-cluster environments with hands-on experience in automated deployments, RBAC/AD integration, and networking troubleshooting.'
            },
            {
                'icon': 'fa-brain',
                'title': 'AI/ML Innovation',
                'description': 'Developing cutting-edge AI solutions with OpenShift AI, Watsonx.ai, and Agentic AI technologies like CrewAI and BeeAI for enterprise applications.'
            }
        ],
        
        'expertise': {
            'Containerization & Orchestration': [
                'Kubernetes', 'OpenShift', 'Docker', 'EKS', 'GKE', 'ROKS', 
                'Kubernetes Administration', 'Multi-cluster Management'
            ],
            'MLOps & AI Tools': [
                'OpenShift AI', 'Watsonx.ai', 'TensorFlow', 'PyTorch', 
                'scikit-learn', 'Prompt Engineering', 'NLTK', 'OpenCV'
            ],
            'Agentic AI': [
                'CrewAI', 'BeeAI'
            ],
            'DevOps & CI/CD': [
                'Jenkins', 'Ansible', 'GitHub', 'Terraform', 'Maven', 
                'Continuous Integration', 'Continuous Delivery'
            ],
            'Cloud Platforms': [
                'IBM Cloud', 'AWS', 'GCP', 'Cloud Networking', 'Cloud Security'
            ],
            'Programming': [
                'Python', 'Linux Scripting', 'Java'
            ],
            'Monitoring & Tools': [
                'Prometheus', 'Grafana', 'LogDNA', 'ServiceNow', 'Postman'
            ],
            'Databases & Storage': [
                'MongoDB', 'MySQL', 'ETCD', 'ODF', 'OpenShift Container Storage'
            ]
        },
        
        'projects': [
            {
                'title': 'IBM Cloud Solutioning Chatbot',
                'icon': 'fa-robot',
                'technologies': ['CrewAI', 'BeeAI', 'Agentic AI'],
                'description': 'Designed and developed an IBM Cloud Solutioning chatbot to assist solution architects leveraging Agentic AI technologies.',
                'highlights': [
                    'Multi-domain testing across IBM Cloud services',
                    'Knowledge corpus integration from multiple sources',
                    'Comprehensive chatbot testing and validation',
                    'Assists solution architects in cloud design decisions'
                ]
            },
            {
                'title': 'Watsonx.AI Security Prototype',
                'icon': 'fa-shield-alt',
                'technologies': ['Watsonx.AI', 'Security Analysis', 'DevSecOps'],
                'description': 'Developed a cutting-edge prototype to identify deployment code vulnerabilities, providing guidance on remediation and ensuring secure infrastructure deployment.',
                'highlights': [
                    'Proactive vulnerability detection in deployment code',
                    'Targeted notifications for security issues',
                    'Accelerated deployment with maintained security standards',
                    'Reduced deployment time while prioritizing security'
                ]
            },
            {
                'title': 'Enterprise Kubernetes Solutions',
                'icon': 'fa-server',
                'technologies': ['OpenShift', 'Kubernetes', 'Multi-cluster Management'],
                'description': 'Designed and implemented secure, scalable, and high-performance Kubernetes/OpenShift solutions for enterprise clients.',
                'highlights': [
                    'RBAC/AD integration for secure operations',
                    'Automated deployments and patch management',
                    'Multi-cluster environment management',
                    'Detailed architectural diagrams and documentation'
                ]
            }
        ],
        
        'experience': [
            {
                'title': 'Technical Specialist (OpenShift/Kubernetes SME)',
                'company': 'IBM',
                'location': 'Dublin, Ireland',
                'period': 'November 2024 – Present',
                'current': True,
                'responsibilities': [
                    'Designed and implemented secure, scalable, and high-performance Kubernetes/OpenShift solutions for enterprise clients',
                    'Collaborated with sales and architecture teams to align cloud-native designs with client strategy',
                    'Produced detailed architectural diagrams, runbooks, and technical documentation',
                    'Acted as a subject-matter expert (SME) on OpenShift, guiding engineering decisions',
                    'Designed and Developed an IBM Cloud Solutioning chatbot leveraging Agentic AI technologies',
                    'Conducted comprehensive chatbot testing across multiple IBM Cloud domains',
                    'Mentored junior engineers, fostering knowledge transfer and skill development'
                ]
            },
            {
                'title': 'Software Engineer Cloud Support',
                'company': 'IBM',
                'location': 'Dublin, Ireland',
                'period': 'October 2021 – October 2024',
                'current': False,
                'responsibilities': [
                    'Provided cloud support for major IBM clients (BNPP, Caixa Bank, American Airlines)',
                    'Resolved complex issues on IBM Kubernetes Service (IKS) and Red Hat OpenShift (ROKS)',
                    'Collaborated with IBM SRE and RedHat teams to troubleshoot and document root causes',
                    'Created technical documentation, runbooks, and scripts to enhance support operations',
                    'Led knowledge-sharing sessions on FOAK and complex issues',
                    'Earned Certified Kubernetes Application Developer (CKAD) and RedHat OpenShift certifications',
                    'Achieved IBM Certified Technical Advocate – Cloud V3 certification'
                ]
            },
            {
                'title': 'IBM Developer Jumpstart',
                'company': 'IBM',
                'location': 'Dublin, Ireland',
                'period': 'February 2024 – June 2024',
                'current': False,
                'responsibilities': [
                    'Developed a cutting-edge prototype with Watsonx.AI to identify deployment code vulnerabilities',
                    'Provided guidance on remediation and ensured secure infrastructure deployment',
                    'Enabled developers to detect vulnerabilities proactively',
                    'Implemented targeted notifications and prioritized security',
                    'Accelerated deployment and reduced deployment time while maintaining high security standards'
                ]
            },
            {
                'title': 'Cloud Service Engineer',
                'company': 'Aspiegel',
                'location': 'Dublin, Ireland',
                'period': 'August 2020 – August 2021',
                'current': False,
                'responsibilities': [
                    'Monitored and debugged issues across ISP and mobile services',
                    'Collaborated with SRE teams to analyze and document root cause analysis',
                    'Deployed and configured applications on Orange Business Cloud',
                    'Set up monitoring and performed troubleshooting operations',
                    'Developed and deployed scripts to support DevOps/SRE operations'
                ]
            }
        ],
        
        'education': [
            {
                'degree': 'Master of Science',
                'field': 'Intelligent Systems',
                'institution': 'Trinity College, Dublin',
                'location': 'Dublin, Ireland',
                'year': '2019',
                'icon': 'fa-graduation-cap'
            },
            {
                'degree': 'Bachelor of Engineering',
                'field': 'Telecommunications Engineering',
                'institution': 'BMS Institute of Technology and Management',
                'location': 'Bangalore, India',
                'year': '2018',
                'icon': 'fa-university'
            }
        ],
        
        'certifications': [
            {'name': 'IBM Certified Technical Specialist', 'issuer': 'IBM', 'year': '2025'},
            {'name': 'RedHat Certified Specialist in Containers (OpenShift)', 'issuer': 'RedHat', 'year': '2023'},
            {'name': 'Certified Kubernetes Application Developer', 'issuer': 'Linux Foundation', 'year': '2023'},
            {'name': 'IBM Cloud Technical Advocate v3', 'issuer': 'IBM', 'year': '2022'},
            {'name': 'IBM Cloud Operational Excellence & Resilience', 'issuer': 'IBM', 'year': '2023'},
            {'name': 'Watsonx Foundations', 'issuer': 'IBM', 'year': '2023'},
            {'name': 'Operating Kubernetes on IBM Cloud', 'issuer': 'IBM', 'year': '2022'},
            {'name': 'IBM Garage Essentials', 'issuer': 'IBM', 'year': '2022'},
            {'name': 'Certified DevOps Associate', 'issuer': 'CloudTrain', 'year': '2024'},
            {'name': 'Certified Prompt Engineer', 'issuer': 'Blockchain Council', 'year': '2023'}
        ],
        
        'patents': [
            {
                'title': 'Intelligent movement pattern-based data backup and restore to handle data residency restrictions in heterogenous cloud computing environments',
                'status': 'Filed',
                'icon': 'fa-file-alt'
            },
            {
                'title': 'Method to detect posture of software bill of materials to assess software supply chain risk',
                'status': 'Filed',
                'icon': 'fa-file-alt'
            },
            {
                'title': 'SBOM as code for efficient software supply chain',
                'status': 'Filed',
                'icon': 'fa-file-alt'
            },
            {
                'title': 'Time travelling vulnerability visualization to select the best cost route based on software bill of materials and multi-dimensional analysis',
                'status': 'Defensive Publication',
                'icon': 'fa-file-contract'
            }
        ]
    }
    
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
