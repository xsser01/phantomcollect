from setuptools import setup, find_packages

setup(
    name="phantomcollect",
    version="1.0.0",
    author="xsser01",
    author_email="psosoej210@gmail.com",
    description="Advanced Stealth Web Data Collection Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xsser01/phantomcollect",  # ✅ الرابط المضاف
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "phantomcollect": ["templates/*.html"],
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "phantomcollect=phantomcollect.core:start_server",
        ],
    },
    keywords="security, web, data-collection, penetration-testing",
)
