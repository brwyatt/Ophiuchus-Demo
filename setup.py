from setuptools import find_packages
from setuptools import setup


setup(
    name="ophiuchus-demo",
    version="0.1.0",
    author="Bryan Wyatt",
    author_email="brwyatt@gmail.com",
    description=(""),
    license="LGPLv3",
    keywords="aws web website serverless lambda",
    url="https://github.com/brwyatt/Ophiuchus-Demo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={},
    python_requires="~=3.6",
    include_package_data=False,
    entry_points={
        "ophiuchus_demo_api": ["default = demo_api.default:Default"],
        "ophiuchus_demo_web": [
            "default = demo_web.default:Default",
            "debug_print = demo_web.debug_print:Debug",
        ],
    },
    install_requires=["boto3>=1.10.0,<1.11.0", "ophiuchus"],
)
