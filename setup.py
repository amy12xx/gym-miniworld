from setuptools import setup

setup(
    name='gym_miniworld',
    version='2020.1.9',
    keywords='environment, agent, rl, openaigym, openai-gym, gym, robotics, 3d',
    packages=['gym_miniworld', 'gym_miniworld.envs'],
    install_requires=[
        # 'gym>=0.9.0,<=0.17.3',
        # 'numpy>=1.10.0',
        'pyglet>=1.5.11',
    ],
    # Include textures and meshes in the package
    include_package_data=True
)
