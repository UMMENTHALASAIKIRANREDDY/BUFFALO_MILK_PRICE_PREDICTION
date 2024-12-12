Here’s a detailed README file for your GitHub project:

---

# Buffalo Milk Price Prediction Web Application

This is a Flask-based web application designed to predict buffalo milk prices based on the SNF (Solid-Not-Fat) and FAT content of the milk. The prediction model is built using Random Forest Regressor and serves as a demonstration of how machine learning can be integrated with a web application.

## Features
- **Prediction Page:** Allows users to input the SNF and FAT values along with the date to predict the milk price.
- **Historical Predictions:** Displays a table of previously predicted prices with corresponding input data (SNF, FAT, and Date).
- **Model:** The model used for predictions is a Random Forest Regressor, which is loaded from a `.pkl` file.

## Setup

### Requirements
- Python 3.x
- Flask
- Pandas
- scikit-learn

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the Random Forest Regressor model file (`rf_regressor_model.pkl`) in the same directory as the Flask application. **Note:** The model file is large, and you can download it by running the script `model_downloading_program.py` located in the `python programs` folder.

   To download the model, simply run:

   ```bash
   python python_programs/model_downloading_program.py
   ```

### Running the Application

To run the web application, use the following command:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/` in your browser.

### Usage

1. Open the index page where you can input the SNF, FAT values, and the date.
2. Submit the form, and the predicted milk price will be displayed.
3. Navigate to the "Prediction History" page to view all previously made predictions with their respective details.

### CSV File

The predictions are saved in a CSV file named `predicted.csv`. This file is updated each time a prediction is made and contains the following columns:
- `RateDate`: The date when the prediction was made.
- `SNF`: The Solid-Not-Fat content of the milk.
- `FAT`: The FAT content of the milk.
- `Rate`: The predicted price of the buffalo milk.
- `PredictionTime`: The timestamp when the prediction was generated.

### Notes
- Since the `.pkl` model file is large, we do not include it directly in the repository. Please use the `model_downloading_program.py` script to download it.
- You can easily update the model or prediction logic by modifying the `rf_regressor_model.pkl` file or the `predict_rate` function in the Flask app.

### File Structure

```
.
├── app.py                    # Main Flask application
├── predicted.csv             # Stores prediction history
├── python_programs/           # Folder containing Python scripts like model downloader
│   └── model_downloading_program.py  # Script to download the model
├── requirements.txt          # Python dependencies
└── templates/
    ├── index.html            # HTML form for user input
    └── prediction.html       # HTML table to display prediction history
```


Here’s a brief section for inputs and outputs that you can include in your README:

## Input

- **RateDate**: The date on which the prediction is to be made (format: `YYYY-MM-DD`).
- **SNF**: Solid-Not-Fat content (numeric value, e.g., 8.5).
- **FAT**: FAT content (numeric value, e.g., 3.5).

### Example Input:

- **RateDate**: `2024-12-12`
- **SNF**: `8.5`
- **FAT**: `3.5`

## Output

- **Predicted Rate**: The predicted price of buffalo milk based on the input values.
- **Prediction Time**: The timestamp when the prediction was made.

### Example Output:

- **Predicted Rate**: `45.30` (price in your chosen currency)
- **Prediction Time**: `2024-12-12 14:30:00`

### Prediction History (Stored in CSV):

Each prediction is stored with the following columns:

- **RateDate**: The input date for the prediction.
- **SNF**: The input SNF value.
- **FAT**: The input FAT value.
- **Rate**: The predicted price.
- **PredictionTime**: The time when the prediction was generated.

---

This section describes the input format for users and the outputs they will receive. You can adjust the values as needed depending on your actual prediction model and output format.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you need any adjustments or further details added!
