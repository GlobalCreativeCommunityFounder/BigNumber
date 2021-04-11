from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='BigNumber',
    version='1',
    packages=['BigNumber'],
    url='https://github.com/GlobalCreativeCommunityFounder/BigNumber',
    license='MIT',
    author='GlobalCreativeCommunityFounder',
    author_email='globalcreativecommunityfounder@gmail.com',
    description='This package contains implementation of the tool "ORTEIL_IDLE_GAME_MAKER_CODE_GENERATOR".',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "ORTEIL_IDLE_GAME_MAKER_CODE_GENERATOR=ORTEIL_IDLE_GAME_MAKER_CODE_GENERATOR.orteil_idle_game_maker_code_generator:main",
        ]
    }
)