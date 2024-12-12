Buffalo Milk Price Prediction Web Application
This is a Flask-based web application designed to predict buffalo milk prices based on the SNF (Solid-Not-Fat) and FAT content of the milk. The prediction model is built using Random Forest Regressor and serves as a demonstration of how machine learning can be integrated with a web application.

Features
Prediction Page: Allows users to input the SNF and FAT values along with the date to predict the milk price.
Historical Predictions: Displays a table of previously predicted prices with corresponding input data (SNF, FAT, and Date).
Model: The model used for predictions is a Random Forest Regressor, which is loaded from a .pkl file.
Setup
Requirements
Python 3.x
Flask
Pandas
scikit-learn
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd <project_directory>
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Place the Random Forest Regressor model file (rf_regressor_model.pkl) in the same directory as the Flask application. Note: The model file is large, and you can download it by running the script model_downloading_program.py located in the python programs folder.

To download the model, simply run:

bash
Copy code
python python_programs/model_downloading_program.py
Running the Application
To run the web application, use the following command:

bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your browser.

Usage
Open the index page where you can input the SNF, FAT values, and the date.
Submit the form, and the predicted milk price will be displayed.
Navigate to the "Prediction History" page to view all previously made predictions with their respective details.
CSV File
The predictions are saved in a CSV file named predicted.csv. This file is updated each time a prediction is made and contains the following columns:

RateDate: The date when the prediction was made.
SNF: The Solid-Not-Fat content of the milk.
FAT: The FAT content of the milk.
Rate: The predicted price of the buffalo milk.
PredictionTime: The timestamp when the prediction was generated.
Notes
Since the .pkl model file is large, we do not include it directly in the repository. Please use the model_downloading_program.py script to download it.
You can easily update the model or prediction logic by modifying the rf_regressor_model.pkl file or the predict_rate function in the Flask app.
File Structure
bash
Copy code
.
├── app.py                    # Main Flask application
├── predicted.csv             # Stores prediction history
├── python_programs/           # Folder containing Python scripts like model downloader
│   └── model_downloading_program.py  # Script to download the model
├── requirements.txt          # Python dependencies
└── templates/
    ├── index.html            # HTML form for user input
    └── prediction.html       # HTML table to display prediction history
License
This project is licensed under the MIT License - see the LICENSE file for details.
