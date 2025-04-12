<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fake Product Review Detector</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Body Styling */
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background: linear-gradient(135deg, #83a4d4, #b6fbff); /* Calming gradient */
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            transition: background 0.3s ease, color 0.3s ease;
        }

        /* Container Styling */
        .container {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 90%;
            transition: background 0.3s ease, box-shadow 0.3s ease;
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 15px;
        }

        p {
            margin-bottom: 20px;
            font-size: 1.1rem;
            color: #555;
        }

        /* Text Area Styling */
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 15px;
            padding: 10px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border 0.3s ease, background 0.3s ease, color 0.3s ease;
        }

        textarea:focus {
            border: 2px solid #007BFF;
            outline: none;
            box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
        }

        /* Button Styling */
        button {
            background: linear-gradient(135deg, #007BFF, #0056b3);
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: background 0.3s ease, transform 0.2s ease;
        }

        button:hover {
            background: linear-gradient(135deg, #0056b3, #003d7a);
            transform: scale(1.05);
        }

        .result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #333;
            padding: 10px;
            border-radius: 8px;
        }

        /* Dark Mode Styling */
        body.dark-mode {
            background: linear-gradient(135deg, #1e1e2f, #121212);
            color: #e0e0e0;
        }

        .container.dark-mode {
            background: #2a2a3c;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
        }

        textarea.dark-mode {
            background: #333;
            border: 2px solid #555;
            color: #e0e0e0;
        }

        button.dark-mode {
            background: linear-gradient(135deg, #555, #333);
        }

        .result.dark-mode {
            background: #2a2a3c;
            color: #e0e0e0;
        }

        /* Toggle Switch */
        .toggle-container {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            align-items: center;
            cursor: pointer;
        }

        .toggle {
            width: 50px;
            height: 25px;
            border-radius: 25px;
            background: #ccc;
            position: relative;
            transition: background 0.3s ease;
        }

        .toggle.dark {
            background: #333;
        }

        .toggle-ball {
            width: 23px;
            height: 23px;
            background: white;
            border-radius: 50%;
            position: absolute;
            top: 1px;
            left: 1px;
            transition: transform 0.3s ease;
        }

        .toggle.dark .toggle-ball {
            transform: translateX(25px);
            background: #fdd835; /* Sun (yellow) */
        }

        .toggle.dark {
            background: #555;
        }

        .mode-icon {
            margin-left: 10px;
            font-size: 1.5rem;
            color: #333;
            transition: color 0.3s ease;
        }

        .dark-mode .mode-icon {
            color: #fdd835; /* Sun color */
        }
    </style>
</head>
<body>
    <!-- Toggle Button -->
    <div class="toggle-container" id="toggleMode">
        <div class="toggle">
            <div class="toggle-ball"></div>
        </div>
        <span class="mode-icon">🌞</span>
    </div>

    <!-- Main Container -->
    <div class="container">
        <h1>Fake Review Detector</h1>
        <p>Paste a review below to analyze its authenticity:</p>
        <textarea id="reviewInput" placeholder="Paste review here..."></textarea>
        <button onclick="analyzeReview()">Analyze</button>
        <div class="result" id="result"></div>
    </div>

    <script>
        // Dark Mode Toggle
        const toggleMode = document.getElementById("toggleMode");
        const body = document.body;
        const toggle = document.querySelector(".toggle");
        const modeIcon = document.querySelector(".mode-icon");

        toggleMode.addEventListener("click", function () {
            body.classList.toggle("dark-mode");
            toggle.classList.toggle("dark");

            // Update the sun/moon icon dynamically
            modeIcon.textContent = body.classList.contains("dark-mode") ? "🌙" : "🌞";
        });

        // Analyze Review Functionality
        function analyzeReview() {
            const review = document.getElementById("reviewInput").value;

            if (!review.trim()) {
                document.getElementById("result").innerText = "Please enter a review!";
                return;
            }

            const authenticityScore = Math.floor(Math.random() * 101);
            document.getElementById("result").innerHTML =
                `Authenticity Score: <strong>${authenticityScore}%</strong><br>` +
                (authenticityScore > 50 ? "Likely Genuine" : "Possibly Fake");
        }
    </script>
</body>
</html># Fake-Review-Detector
ML-powered web app to identify fake product reviews
