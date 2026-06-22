from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else "SPOTPY"

setup(
	use_scm_version={"write_to": "src/spotpy/_version.py"},
	setup_requires=["setuptools_scm[toml]>=6.4"],
	name="spotpy",
	description="A Statistical Parameter Optimization Tool.",
	long_description=README,
	long_description_content_type="text/markdown",
	author="Tobias Houska and contributors",
	packages=find_packages("src"),
	package_dir={"": "src"},
	include_package_data=True,
	python_requires=">=3.10",
	install_requires=["numpy>=2.0", "scipy>=1.5.0"],
	extras_require={
		"plotting": ["pandas>=1", "matplotlib>=3"],
		"test": [
			"pytest-cov>=3",
			"numba",
			"pathos",
			"matplotlib",
			"click",
			"pandas",
			"tables",
			"docutils",
		],
	},
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
	],
	zip_safe=False,
)

