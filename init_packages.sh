pip install --upgrade pip
pip install build

pip install -e packages/inference

cd packages/inference/
python -m build --sdist --wheel
cd dist
cp *.whl ../../../cats_dogs_other/train/packages
cd ../../../