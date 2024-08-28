# Smart Movie Recommendation System

## Introduction

This project is a smart movie recommendation system designed to enhance the user experience by providing personalized movie recommendations based on user preferences, popular trends, and highly rated movie.

## Features

- **Personalized Movie Recommendations:** Based on user history, preferences, and popular movie trends.
- **Cross-Platform Compatibility:** Developed using Kotlin to run on multiple operating systems.
- **Firebase Analytics Integration:** Monitors user interactions to improve recommendation accuracy.
Movie Recommendation System:
<div align="center"> <table> <tr> <td align="center"> <strong>Step 1: Selecting Preferred Movies</strong><br> <img src="https://github.com/user-attachments/assets/cb964516-2a7f-4d75-aece-d5e27ad4d64f" alt="User Selecting Movies" width="300"> </td> <td align="center"> <strong>Step 2: Display of Liked Movies</strong><br> <img src="https://github.com/user-attachments/assets/c9951b84-6c6a-4199-9191-1851525d6c74" alt="Liked Movies Overview" width="300"> </td> <td align="center"> <strong>Step 3: Personalized Movie Recommendations</strong><br> <img src="https://github.com/user-attachments/assets/79b69044-ddb0-4306-b10e-1dc42cf9d481" alt="Recommended Movies" width="300"> </td> </tr> </table> </div>

## Modules

1. **User:** Interacts with the application to receive movie recommendations.
2. **Application:** The core module where movie is recommended and played.
3. **Algorithm Service:** Utilizes machine learning algorithms (content-based and collaborative filtering) to generate recommendations.
4. **Database:** Stores user profiles and movie preference.

## Project Design

### Existing System
Most current music recommendation systems rely on user profile analysis using basic filtering techniques. These systems often lack innovation and do not fully consider user preferences.

### Proposed System
The proposed system uses a hybrid recommendation approach, combining content-based and collaborative filtering to provide more accurate and personalized music recommendations. The system also suggests related videos and integrates a voice assistant for hands-free usage.

### Steps to Download and Use

1. **Clone the Repository**
```bash
git clone https://github.com/arjunnrajput/Smart-ML-Based-Movie-Recommendation-System/ml
```
2. **Open in Android Studio**
- Open Android Studio and select `Open an existing project`.
- Navigate to the cloned directory and open it.

3. **Configure Firebase**
- Create a new project in the Firebase Console.
- Download the `google-services.json` file from Firebase and place it in the `app/` directory of your project.
- Enable Firebase Analytics in your project.

4. **Build the Project**
- Sync the project with Gradle files.
- Build the project to ensure all dependencies are resolved.

5. **Run the App**
- Connect an Android device or use an emulator.
- Click the `Run` button in Android Studio to install the app on your device.

6. **Test Features**
- Register or log in to the app.
- Explore the music recommendations, like your favorite tracks, and test voice commands.

## Implementation Steps

1. **Get Sample Code:** Start with the provided codebase.
2. **Import Starter App:** Import the project into Android Studio.
3. **Create Firebase Console Project:** Set up Firebase for data management and analytics.
4. **Run the Starter App:** Launch the initial version on a device.
5. **Add Firebase Analytics:** Integrate to track user interactions.
6. **Export Data to BigQuery:** Analyze data for model training.
7. **Preprocess and Train Model:** Use TensorFlow Lite for the recommendation model.
8. **Integrate the Model:** Implement the trained model into the app.
9. **Run the App:** Test the final version with movierecommendations.

## Testing

- **Unit Testing:** Ensures the functionality of the recommendation system, particularly the movie recommendation.


## Conclusion and Future Scope

The Smart Movie Recommendation System successfully delivers personalized movie recommendations. Future improvements may include refining the recommendation algorithms and expanding the system's features based on user feedback.
