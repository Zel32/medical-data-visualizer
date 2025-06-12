# 🩺 Medical Data Visualizer

This project is part of the **[freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)**. It uses real-world medical data to create visualizations that help identify trends and correlations related to cardiovascular health.

---

## 📁 Project Structure

```
.
├── main.py                     # Entrypoint to generate plots and run unit tests
├── test_module.py             # Unit tests for data visualization functions
├── medical_data_visualizer.py # Visualization logic (imported in main.py)
├── medical_examination.csv    # Medical data source file (from freeCodeCamp)
├── catplot.png                # Output image: categorical plot
├── heatmap.png                # Output image: correlation heatmap
```

---

## 📊 Project Overview

The project consists of two main visualizations:

### ✅ Categorical Plot (`catplot.png`)
- Created using `sns.catplot()`
- Displays the distribution of health-related features:
  - `active`
  - `alco`
  - `cholesterol`
  - `gluc`
  - `overweight`
  - `smoke`
- Split by cardiovascular disease (`cardio = 0` or `1`)

### ✅ Heatmap (`heatmap.png`)
- Uses filtered data to remove incorrect and extreme values
- Shows the correlation matrix of medical features
- Visualized using `sns.heatmap()` with a masked upper triangle and annotations

---

## ⚙️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/medical-data-visualizer.git
   cd medical-data-visualizer
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas seaborn matplotlib numpy
   ```

3. **Ensure the dataset `medical_examination.csv` is present in the project directory.**

4. **Run the main script**:
   ```bash
   python main.py
   ```

This will:
- Generate `catplot.png` and `heatmap.png`
- Automatically run unit tests defined in `test_module.py`

---

## 🧪 Testing

The repository includes unit tests for validation of visualization outputs:

- **`test_module.py`** tests:
  - Axis labels and categories in the categorical plot
  - Label coverage and annotated values in the heatmap

Tests are run automatically when executing `main.py`.

---

## 📚 What I Learned

- Data preprocessing and feature engineering using Pandas and NumPy
- Creating clean and informative visualizations using Seaborn and Matplotlib
- Filtering and normalizing real-world datasets
- Writing and running unit tests for visualization-based outputs

---

## 📜 License

This project is part of the **freeCodeCamp Data Analysis with Python** curriculum and is shared for educational purposes only.

---

## 🙌 Acknowledgments

- [freeCodeCamp](https://www.freecodecamp.org/) for the project and learning platform
- The open-source Python data science community for excellent tools
