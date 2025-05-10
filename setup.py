from setuptools import setup, find_packages

setup(
    name="HaritaSEOAsistani",
    version="1.0.0",
    author="Kerem Atalay",
    author_email="keremazra61@gmail.com",
    description="Google Haritalar için AI destekli yorum ve pinleme aracı.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "requests",
        "openai",
        "faker",
        "python-dotenv",
        "beautifulsoup4",
        "selenium",
        "webdriver-manager",
        "pillow",
        "email-validator",
        "schedule",
        "user-agents",
        "bcrypt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
