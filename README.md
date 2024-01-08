## Smart Attendance System based on Dual Bio-Metric Approach

This is the Final Year Project of our course curriculum ( Bachelor of Technology in
Information Technology from Techno Main Saltlake, Kolkata, West Bengal).

- Smart Attendance System based on Dual Bio-Metric Approach using Face Recognition(implemented) and Fingerprint Recognition(not yet implemented)

### Team Details
 1. Aryadeep Chakraborty (Univ. Roll No. - 13000221116)
 2.  Aritra Ganguly (Univ. Roll No. - 13000220087)
 3. Aditya Kant (Univ. Roll No. - 13000220086)
 4. Md Nafees Uddin (Univ. Roll No. - 13000220085)

Under the Supervision of **Dr. Anirban Goswami**


<img src="https://thumbs4.imagebam.com/88/b6/15/MEQOIX4_t.jpg" alt="Techno Main Saltlake" width="50"/>

**Department of Information Technology 
Techno Main Salt Lake. 
Kolkata -700091.**
##


### Table of Contents  
|Serial No| Topic |
|--|--|
| 1 | [Objective](#objective)  |
| 2 | [Problem Definition](#problem-definition) |
| 3 | [Literature Review](#literature-review) |
| 4 | [Proposed Methodology](#proposed-methodology) |
| 5 | [Experimental Details](#experimental-details) |
| 6 | [Results and Analysis](#results-and-analysis) |
| 7 | [Conclusion](#conclusion) |
| 8 | [References](#references) |

##

### Objective
<a id="objective"></a>
- The primary problem this system aims to resolve is the inadequacy of traditional attendance management methods in ensuring accuracy and security.
- Automate the process of recording attendance in educational institutions or any organisation.
- Enhance accuracy and efficiency compared to traditional methods.
- Utilize biometric technologies - finger and face recognition.
##

### Problem Definition
<a id="problem-definition"></a>
- The traditional methods of manual attendance tracking in educational institutions are plagued by inefficiency, errors, and susceptibility to proxy attendance. These methods are time-consuming and often lead to inaccuracies. Additionally, the conventional use of ID cards or signatures is prone to forgery.

- Recognizing these challenges, our project addresses the need for an Automated Attendance System using fingerprint and face recognition. By leveraging advanced biometric technologies, we aim to eliminate these shortcomings, providing a reliable, accurate, and secure solution that not only streamlines the attendance process but also ensures accountability and reduces administrative burden.
 ##

### Literature Review
<a id="literature-review"></a>
- The algorithm proposed by **Sharat S. Chikkerur, et al. [1]**, uses an approach for fingerprint image enhancement based on Short Time Fourier Transform (STFT) Analysis to analyze non-stationary signals.

- In another algorithm by **Kadry S., et al. [2]**, proposes a design and implementation of a wireless iris recognition attendance management system. This system is an application of the iris recognition verifying and RF wireless techniques.

- **Samuel Lukas, et al. [3]**,  proposes an algorithm where facial recognition is finished entirely by performing grayscale standardization, histogram balance, Discrete Wavelet Transform (DWT) and Discrete Cosine Transform (DCT).

- As proposed by **Dhanush Gowda H.L, et al. [4]**,  uses an integrated camera module for attendance taking. The video of the class is recorded & from that video footage attendance is taken by recognizing the faces of each one present in the classroom.
 ##

### Proposed Methodology
<a id="proposed-methodology"></a>
Our proposed methodology integrates various technologies to create a robust Automated Attendance System that leverages fingerprint and face recognition.

The following steps outline the key components of our approach:

**1.Data Collection:**

- Fingerprint Data: Utilize a fingerprint scanner to capture unique features (minutiae points) of each  student's fingerprint. Store this data securely in a MySQL database.

- Facial Data: Implement a webcam with OpenCV to capture facial images. Use Haar-Cascade Classifier for facial feature extraction and store the data in the database.

**2. Database Management:**

- MySQL Database: Store fingerprint and facial data in a centralized MySQL database for efficient retrieval and comparison during attendance tracking.

**3. User Interface:**

- Python and Tkinter: Develop a user-friendly interface using Python and Tkinter to interact with the system. This interface will allow administrators to manage the database and track attendance.

**4. Face Recognition:**

- OpenCV and Haar-Cascade Classifier: Utilize OpenCV along with Haar-Cascade Classifier to detect and extract facial features. Compare the features to recognize and identify students.

**5. Fingerprint Recognition:**

- OpenCV and Minutiae Extraction: Employ OpenCV for image processing and minutiae extraction from fingerprint scans. Compare extracted minutiae with the stored data for fingerprint recognition.

**6.  Attendance Marking:**

- Integration: Combine the results from fingerprint and face recognition for a more robust attendance marking system. If both modalities confirm the student's identity, mark them as present.
##

### Experimental Details
<a id="experimental-details"></a>
**1. Hardware Setup :**
- Webcam: Laptop camera/any external webcam
- Fingerprint Scanner: R307 (not yet implemented)
- Computing Device: Desktop/Laptop

**2. Software Environment :**
- Programming Language: Python
- GUI Library: Tkinter
- Image Processing Library: OpenCV
- Database Management: MySQL
- Image Analysis: PIL

**3.  Dataset :**
- Biometric Data: Face & Fingerprint (not yet implemented) with individual’s specific ID

**4.  Data Preprocessing:**
- Facial Data: Grayscale standardization, histogram balance, DWT, and DCT
- Fingerprint Data: STFT-based enhancement using OpenCV (not yet implemented)
##

### Results and Analysis
<a id="results-and-analysis"></a>

<img src="https://thumbs4.imagebam.com/d8/7d/bf/MEQOIT2_t.png" alt="Fig: Known Face 1" width="300"/>
<img src="https://thumbs4.imagebam.com/01/32/45/MEQOIT3_t.png" alt="Fig: Known Face 2" width="300"/>

Fig : Known Face 1 & 2

<img src="https://thumbs4.imagebam.com/24/08/14/MEQOIT4_t.png" alt="Fig: Unknown Face" width="300"/>

Fig: Unknown Face

**Result:** 
<img src="https://thumbs4.imagebam.com/9f/b4/59/MEQOIWA_t.png" alt="Fig: Result" width="700"/>

- Accuracy: High accuracy achieved in face recognition.
##

### Conclusion
<a id="conclusion"></a>
- The integration of face and fingerprint-based attendance systems marks a significant advancement in the realm of workforce management.

- The fusion of biometric recognition technologies not only ensures a highly accurate and reliable method for tracking attendance but also brings forth efficiency and time-saving benefits.

- The automated processes minimize the potential for errors associated with manual data entry, while the inherent security of biometric data adds an extra layer of protection against unauthorized access.

- The future scope of face and fingerprint-based attendance systems is poised for continual evolution and enhancement.

Overall, the trajectory of these systems points toward a more sophisticated, interconnected, and user-friendly approach to attendance tracking across various sectors.

##

### References
<a id="references"></a>
1. Sharat S. Chikkerur, “Online Fingerprint Verification System”, Department of Electrical Engineering, Faculty of the Graduate School of the State University of New York at Buffalo, 2005

2. Kadry S. and Smaili M., “Wireless Attendance Management System based on Iris Recognition”, Scientific Research and Essays Vol. 5(12), pp. 1428-1435, 18 June, 2010.

3. Samuel Lukas, Aditya Rama Mitra, Ririn Ikana Desanti, Dion Krisnadi, “Student Attendance System in Classroom Using Face Recognition Technique”, Conference Paper-October 2016, Indonesia.

4. Dhanush Gowda H.L, K Vishal, Keerti raj B. R, Neha Kumari Dubey, Pooja M. R, “Face Recognition based Attendance System”, International Journal of Engineering Research & Technology (IJERT), ISSN: 2278-0181, June-2020.

5. Shrey Bhagat, Vithal Kashkari, Shubhangi Srivastava, Ashutosh Sharma, “Face Recognition Attendance System”, International Journal for Research in Applied Science & Engineering Technology (IJRASET) ISSN: 2321-9653, Jan 2022.