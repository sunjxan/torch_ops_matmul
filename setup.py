from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
ext_modules = [
    CUDAExtension(
        "torch_ops_matmul", [
            "src/cuda/matmul.cu"
        ],
        include_dirs=[
        ]
    ) 
]
setup(
    name="torch_ops",
    version="1.0",
    packages=find_packages("src"),
    package_dir={"":"src"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
    zip_safe=False
)
