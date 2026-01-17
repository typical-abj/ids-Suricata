*Detection Effectiveness*
--------------------------
Suricata was effective at detecting known attack patterns such as port scans and basic brute-force attempts using default and modified rules.

Signature-based detection worked reliably when traffic matched expected patterns.

*False Positives*
-----------------

Several alerts were triggered by normal network activity, particularly during testing with background services.

Rule tuning and threshold adjustments were necessary to reduce noise and improve alert relevance.

*Configuration and Setup Challenges*
------------------------------------

Initial configuration required careful attention to network interface selection and logging paths.

Misconfigured rules or improper thresholds resulted in excessive alerts, highlighting the importance of controlled tuning.

*Performance Observations*
---------------------------

The system remained stable under low to moderate traffic volumes.

Increased traffic resulted in higher alert frequency, reinforcing the need for filtering and prioritization mechanisms.

*Key Takeaways*
---------------

Rule-based IDS solutions are effective for known threats but limited against unknown or zero-day attacks.

Proper configuration and tuning are critical to making IDS output usable.

Visibility through a simple web interface significantly improved the ability to review and analyze alerts.

*Areas for Improvement*
------------------------
Implement anomaly-based detection to complement signature-based rules.

Improve alert filtering and prioritization.

Optimize performance for higher traffic environments.
