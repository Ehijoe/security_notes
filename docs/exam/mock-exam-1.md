# Mock exam 1

<div class="exam-header" markdown>

**CSC 583: Computer and Information Security — Mock examination 1**

**Time allowed:** 2 hours

**Instructions:** Answer **Question 1** and any other **TWO** questions. Each question carries **20 marks**.

*This paper follows the format assumed on the [exam technique](exam-technique.md#the-paper) page. The real paper's instructions may differ.*

</div>

Sit it under time, with the answers closed. Then mark your script against the model answers and marking points. The table at the end shows which unit each question tests.

---

## Question 1 (compulsory)

**1a.** Define *vulnerability*. <span class="marks">(2 marks)</span>

??? success "Model answer"
    A vulnerability is a "weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a threat source." ([Unit 1](../unit-1-security-concepts.md#computer-security-terminology))

    **Marking points:** weakness in a system, procedures, controls or implementation (1); could be exploited or triggered by a threat source (1).

**1b.** Name the three impact levels of a security breach and the kind of adverse effect each describes. <span class="marks">(2 marks)</span>

??? success "Model answer"
    - **Low:** a *limited* adverse effect.
    - **Moderate:** a *serious* adverse effect.
    - **High:** a *severe or catastrophic* adverse effect.

    ([Unit 1](../unit-1-security-concepts.md#impact-levels-of-a-security-breach))

    **Marking points:** three levels (1); the matching effect for all three (1).

**1c.** State the four categories of assets of a computer system. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Hardware; software; data; communication facilities and networks. ([Unit 1](../unit-1-security-concepts.md#assets-of-a-computer-system))

    **Marking points:** ½ per category.

**1d.** Distinguish between a passive attack and an active attack. <span class="marks">(2 marks)</span>

??? success "Model answer"
    A **passive attack** attempts to learn or make use of information from the system but does not affect system resources; it only monitors (e.g. eavesdropping), so it threatens confidentiality. An **active attack** attempts to alter system resources or affect their operation (e.g. masquerade, replay, modification of messages). ([Unit 2](../unit-2-attacks.md#what-a-security-attack-is))

    **Marking points:** passive (1); active (1).

**1e.** State the two firewall functions discussed under §6.4 and what each does. <span class="marks">(2 marks)</span>

??? success "Model answer"
    - **NAT (Network Address Translation):** changes the destination or source addresses of data packets as they pass through a firewall, so multiple devices can connect to the internet using the same IP address.
    - **VPN (Virtual Private Network):** extends the private network across a public one such as the internet, so users can transmit data securely as if their devices were directly connected to the private network.

    ([Unit 5](../unit-5-firewalls.md#firewall-functions-nat-and-vpn))

    **Marking points:** NAT with its function (1); VPN with its function (1).

**1f.** Name the three malware protection stages. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Pre-execution detection; runtime detection; post-execution response. ([Unit 9](../unit-9-malware.md#the-three-malware-protection-stages))

    **Marking points:** all three (2); any two (1).

**1g.** Define *privacy* as used in the discussion of ethical issues. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Privacy refers to an individual's right to control how personal information about them is collected, used, stored, and disclosed. ([Unit 10](../unit-10-ethics-legal.md#privacy))

    **Marking points:** individual's right to control personal information (1); collected, used, stored and disclosed (1).

**1h.** List four common vulnerabilities of operating systems. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Any four of: unpatched software; misconfigured settings; default passwords; buffer overflows; privilege escalation; open network ports; insecure APIs; malware injection. ([Unit 3](../unit-3-os-security.md#vulnerabilities-of-operating-systems))

    **Marking points:** ½ per vulnerability.

**1i.** Give the release years of WEP and WPA3. <span class="marks">(2 marks)</span>

??? success "Model answer"
    WEP: **1997**. WPA3: **2018**. ([Unit 7](../unit-7-wireless-mobile.md#the-four-wireless-network-security-protocols))

    **Marking points:** 1 each.

**1j.** Name the three primary classes of IDPS detection methodology. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Signature-based detection; anomaly-based detection; stateful protocol analysis. ([Unit 12](../unit-12-idps.md#idps-detection-methodologies))

    **Marking points:** all three (2); any two (1).

---

## Question 2

**2a.** Define *symmetric encryption* and *asymmetric encryption*, and name two algorithms of each kind. <span class="marks">(6 marks)</span>

??? success "Model answer"
    **Symmetric encryption** is a method of scrambling data using a single shared secret key: whoever holds that key can both encrypt and decrypt the information. It is also called "secret key cryptography", "private key cryptography" or "symmetric key encryption". Algorithms: **AES** (AES-128, AES-192, AES-256), DES, Triple DES (3DES), Blowfish, RC4/RC5/RC6.

    **Asymmetric encryption**, also known as public-key cryptography, uses a **pair of keys** to encrypt and decrypt data: a public key, which can be shared with anyone, and a private key, which is kept secret. The sender encrypts with the recipient's public key, and the recipient decrypts with their private key. Algorithms: **RSA**, ECC, Diffie-Hellman (DH), DSA.

    ([Unit 4: symmetric](../unit-4-cryptography.md#symmetric-encryption), [asymmetric](../unit-4-cryptography.md#asymmetric-encryption))

    **Marking points:** symmetric definition (2); asymmetric definition, with both keys (2); two correct algorithms of each kind (1 + 1).

**2b.** State and explain the six properties of cryptographic hash functions. <span class="marks">(6 marks)</span>

??? success "Model answer"
    - **Deterministic:** the same input always generates exactly the same hash output, so verification is consistent and reliable.
    - **Fast computation:** inputs are processed quickly and efficiently, which makes hashing practical for large datasets and real-time applications.
    - **Pre-image resistance:** it is computationally infeasible to recover the original input from its hash value.
    - **Second pre-image resistance:** given an input and its hash, it is extremely difficult to find a *different* input with the same hash, which prevents forgery.
    - **Collision resistance:** the chance that two distinct inputs produce the same hash is minimised.
    - **Avalanche effect:** even a tiny change in the input, such as flipping one bit, causes a large and unpredictable change in the hash.

    ([Unit 4](../unit-4-cryptography.md#properties-of-cryptographic-hash-functions))

    **Marking points:** 1 per property with its explanation (1 × 6).

**2c.** *PayNaija* (a fictional Lagos fintech) has three security needs:

- It stores several gigabytes of transaction logs on its servers every day and wants them unreadable if a server is stolen.
- Its mobile app must receive a fresh secret session key from the server over the internet without the key being exposed.
- It sends customers monthly PDF statements and wants customers to be able to confirm that each statement came from PayNaija and has not been altered.

For each need, recommend symmetric encryption, asymmetric encryption or a hash-based digital signature. Justify each choice and say why the alternatives fit less well. <span class="marks">(8 marks)</span>

??? success "Model answer"
    **Need 1: bulk logs at rest → symmetric encryption (e.g. AES-256).**

    - **Why:** a single shared key encrypts and decrypts, and symmetric algorithms are fast, so they suit large volumes of data. AES is described as the gold standard today.
    - **Why not the others:** asymmetric encryption is slower and is used mainly for small data, signatures and key exchange. A hash can't be reversed, so PayNaija could never read its own logs again.

    **Need 2: sending a session key → asymmetric encryption (key exchange).**

    - **Why:** asymmetric encryption allows **secure key exchange**. The server can encrypt the session key with the app's public key, or the two can use Diffie-Hellman, so no secret key ever needs to be sent in the clear.
    - **Why not the others:** symmetric encryption would need a key that is already shared, which is the very problem to be solved. Hashing gives no confidentiality.

    **Need 3: authentic, unaltered statements → hash-based digital signature.**

    - **Why:** PayNaija hashes each statement and encrypts the hash with its **private key** to form the signature, then appends it. The customer hashes the statement, decrypts the signature with PayNaija's **public key** and compares the two. A match proves origin (authenticity) and that nothing changed (integrity).
    - **Why not the others:** encrypting the statement would hide it but wouldn't prove who sent it. A bare hash could be recomputed by anyone who altered the file.

    ([Unit 4: choosing between them](../unit-4-cryptography.md#choosing-between-symmetric-asymmetric-and-hashing), [signing](../unit-4-cryptography.md#signing-a-document-the-hash-based-model), [verifying](../unit-4-cryptography.md#verifying-a-digital-signature))

    **Marking points:** need 1 choice and justification (2), why not the alternatives (1); need 2 choice and justification (1), why not (1); need 3 choice with the signing and verifying steps (2), why not (1).

---

## Question 3

**3a.** List the five types of access control systems, and explain **any two** of them. <span class="marks">(6 marks)</span>

??? success "Model answer"
    The five types are discretionary access control (DAC), mandatory access control (MAC), role-based access control (RBAC), attribute-based access control (ABAC) and rule-based access control (RuBAC).

    - **ABAC:** in contrast to RBAC, ABAC is a complex strategy that assigns or denies access to users based on a set of **attributes** (assigned by the owner or administrator), rather than on job role alone.
    - **RuBAC:** involves **defining the rules** that govern access to a resource. The rules are often based on conditions, e.g. "only users in the finance department can access financial data".

    *(Explaining DAC, MAC or RBAC is equally acceptable.)* ([Unit 8](../unit-8-access-control.md#types-of-access-control-systems))

    **Marking points:** the five types (½ each, rounded up to 3); each explanation (1½ × 2).

**3b.** State **six** of the ten database security best practices. Then explain how **two** of them help against insider threats. <span class="marks">(6 marks)</span>

??? success "Model answer"
    The ten practices are:

    1. apply proper access controls;
    2. separate database servers;
    3. encrypt data in transit and at rest;
    4. use database firewalls;
    5. strengthen authentication;
    6. monitor database activity;
    7. implement backup and disaster recovery;
    8. patch and update regularly;
    9. limit physical access;
    10. conduct regular penetration testing.

    Against insider threats:

    - **Apply proper access controls:** define which users can access which resources and apply **least privilege**, so an insider can reach only the data their job needs. This limits the damage from excessive privileges.
    - **Monitor database activity:** real-time monitoring gives visibility into anomalies and helps security teams identify **insider threats** and external breaches.

    ([Unit 11](../unit-11-database-security.md#database-security-best-practices))

    **Marking points:** ½ per practice stated (½ × 6 = 3); each insider-threat explanation (1½ × 2).

**3c.** A teaching hospital in Ibadan keeps patient records in a database. An audit finds that:

- the night-shift nurses on one ward all log in with a single shared account;
- a doctor who resigned eight months ago still has an active account;
- the database runs on the same server as the public appointment website;
- nightly backups are written, unencrypted, to a disk kept in the same server room.

For each finding, name the weakness using the courseware's terms and recommend a control, with justification. <span class="marks">(8 marks)</span>

??? success "Model answer"
    1. **Shared account → the *password sharing* threat** ([Unit 11](../unit-11-database-security.md#common-database-security-threats)).
        - **Control:** *strengthen authentication*, with a unique account and strong password per nurse plus multi-factor authentication.
        - **Why:** actions can then be traced to one person, which supports accountability, and one leaked password exposes only one account.
    2. **Resigned doctor's account → an *orphaned account*** ([Unit 8](../unit-8-access-control.md#challenges-in-access-control)).
        - **Control:** *access management* covering onboarding and offboarding, and *regular audits* that remove stale credentials.
        - **Why:** an unused but active account is an easy way in for a former employee or anyone who steals the credentials.
    3. **Shared web and database server → breaks the *separate database servers* practice.**
        - **Control:** move the database onto its own server, behind a database firewall.
        - **Why:** separating database servers from web servers minimises **lateral movement**. A compromise of the public website no longer gives direct access to patient records.
    4. **Unencrypted backups in the same room → weak *backup and disaster recovery* and missing encryption at rest.**
        - **Control:** encrypt the backups, and store secure copies **separately** from the database server, testing them frequently so they can be restored.
        - **Why:** a theft or a fire in that room would otherwise destroy or expose both the database and its backup. Encryption makes a stolen copy unreadable.

    **Marking points:** for each finding, the weakness named (1) and a justified control (1) (2 × 4).

---

## Question 4

**4a.** Explain stateless and stateful firewalls, and give one limitation of each. <span class="marks">(6 marks)</span>

??? success "Model answer"
    - **Stateless firewall (packet filtering, first generation):** protects the network by analysing traffic at the **transport layer** and checking each packet against rules such as source and destination address and port. **Limitation:** although fast and inexpensive, it has **zero visibility into packet sequencing**, so it can't tell whether a packet belongs to a legitimate conversation.
    - **Stateful firewall (second generation):** tracks the most recent status of **active connections**, so it can monitor the state and context of network communications and allow only packets that belong to a known connection. **Limitation:** it offers more protection than packet filtering but takes a **greater toll on network performance**, because the analysis is more in-depth.

    ([Unit 5: stateless](../unit-5-firewalls.md#stateless-firewalls-packet-filtering), [stateful](../unit-5-firewalls.md#stateful-firewalls))

    **Marking points:** each explanation (2 × 2); each limitation (1 × 2).

**4b.** Describe signature-based and anomaly-based detection. Give one of the courseware's examples of a signature. <span class="marks">(6 marks)</span>

??? success "Model answer"
    - **Signature-based detection:** a *signature* is a pattern that corresponds to a known attack or type of attack, and signature-based detection compares signatures against observed events to identify possible incidents. It is very effective against **known** attacks but largely ineffective against previously unknown attacks, disguised attacks and many variants of known attacks.
    - **Anomaly-based detection:** compares definitions of what activity is considered **normal** (profiles built over a training period) against observed events, to identify significant deviations. Its major benefit is that it can be very effective at detecting **previously unknown** attacks.
    - **Example signature:** an email with the subject "Free pictures!" and an attachment named "freepics.exe". The other examples are a telnet attempt with the username "root", and an operating system log entry with status code 645 (auditing disabled).

    ([Unit 12: signature](../unit-12-idps.md#signature-based-detection), [anomaly](../unit-12-idps.md#anomaly-based-detection))

    **Marking points:** signature-based (2); anomaly-based (2); example (2).

**4c.** *ShopEko* (a fictional Nigerian e-commerce firm) protects its network with a first-generation packet-filtering firewall only. In one week:

- staff receive a widely reported malware email whose attachment pattern is already published by security vendors;
- a staff account that normally downloads a few megabytes a day downloads 40 GB of customer data at 3 a.m.

Answer the following:

1. Which IDPS detection method would catch each event, and why? <span class="marks">(4 marks)</span>
2. Should ShopEko deploy an IDS or an IPS, and what kind of firewall should replace the packet filter? Justify both. <span class="marks">(4 marks)</span>

??? success "Model answer"
    **(i) Detection.**

    - **Malware email → signature-based detection.** The attack is **known** and its pattern is published, so it can be matched against a signature, just like the courseware's "freepics.exe" example. It is the simplest and most effective method for known attacks.
    - **3 a.m. download → anomaly-based detection.** No signature describes this; it is a big **deviation from the account's normal profile** (time and volume). Anomaly-based detection is built for exactly this. Signature-based detection would miss it, because nothing in the traffic matches a known attack pattern.

    **(ii) IDS or IPS, and the firewall.**

    - **An IPS (or an IDPS used in prevention mode).** An IDS would only alert, and 40 GB could leave before anyone reacted. An IPS can **stop the attack itself**, for example by terminating the connection or blocking the user account ([Unit 12](../unit-12-idps.md#how-an-ips-responds-three-groups-of-response-techniques)).
    - **A next-generation firewall (NGFW).** It blends the best parts of past firewall technologies with advanced capabilities such as **deep packet inspection (DPI)**, **intrusion prevention (IPS)** and **data loss prevention (DLP)**, which blocks intentional and accidental data disclosures, exactly the risk in the 3 a.m. download ([Unit 5](../unit-5-firewalls.md#next-generation-firewalls-ngfw)). A stateful firewall alone tracks connections but doesn't inspect content, so it would let both the email and the download through.

    **Marking points:** (i) each method correctly matched and justified (2 × 2); (ii) IPS with justification (2); NGFW with "why not stateful" (2).

---

## Question 5

**5a.** Define *ethical hacking* and state the five things an ethical hacker should have. <span class="marks">(6 marks)</span>

??? success "Model answer"
    **Ethical hacking** involves authorized security testing performed to identify vulnerabilities and improve security. An ethical hacker should have:

    1. **Authorization:** permission to conduct the test.
    2. **Defined scope:** the systems and activities the test covers.
    3. **Defined objectives:** what the test is intended to determine.
    4. **Rules of engagement:** the conditions under which testing will occur.
    5. **Responsible reporting:** vulnerabilities should be communicated appropriately.

    ([Unit 10](../unit-10-ethics-legal.md#ethical-hacking))

    **Marking points:** definition (1); 1 per requirement (1 × 5).

**5b.** List **eight** components of an information security policy, and explain the *policy statement* and *roles and responsibilities* components. <span class="marks">(6 marks)</span>

??? success "Model answer"
    Any eight of the seventeen: policy statement; roles and responsibilities; access control; identification and authentication; data classification; encryption; remote access; acceptable use; patching; malicious code protections; physical security; backups; server security; employee on/off boarding; change management; incident response; monitoring and auditing.

    - **Policy statement:** the overarching security intentions and direction of the organisation.
    - **Roles and responsibilities:** defines who is responsible for security tasks, e.g. the CISO, IT staff and employees.

    ([Unit 6](../unit-6-security-policy.md#components-of-an-information-security-policy))

    **Marking points:** ½ per component (½ × 8 = 4); each explanation (1 × 2).

**5c.** A microfinance bank in Abuja has no written security policy, and its IT staff turnover is high. It hires a contractor to test its online banking system. Without asking, the contractor also tests the bank's HR server, and copies 2,000 customer records to a personal laptop "to prove how serious the risk is".

Answer the following:

1. Identify two policy weaknesses at the bank. <span class="marks">(2 marks)</span>
2. Evaluate the contractor's conduct against the requirements for ethical hacking and the ethical principles for security professionals. <span class="marks">(4 marks)</span>
3. Recommend two actions for the bank. <span class="marks">(2 marks)</span>

??? success "Model answer"
    **(i) Policy weaknesses** ([Unit 6](../unit-6-security-policy.md#policy-weakness)):

    - **No written security policy:** security efforts evolve and are enforced, if at all, inconsistently.
    - **Employment policies:** frequent staff turnover weakens security knowledge and continuity.

    **(ii) The contractor's conduct** ([Unit 10](../unit-10-ethics-legal.md#ethical-principles-for-security-professionals)):

    - **Scope and authorization:** the HR server was outside the **defined scope** and had no **authorization**. Testing it was unauthorized access, which raises legal as well as ethical issues.
    - **Avoid unnecessary harm and protect information entrusted to them:** copying 2,000 records to a personal laptop goes beyond what is needed to prove a vulnerability, and exposes customers' data.
    - **Respect privacy and maintain confidentiality:** the records are customers' personal financial information.
    - **What should have happened:** document the finding and use **responsible reporting** through the agreed channel, without copying the data.

    **(iii) Recommendations:**

    - Adopt a **written information security policy**, with roles and responsibilities, acceptable use, data classification and incident response.
    - For every future test, sign **rules of engagement** that set scope, objectives and data handling. Treat the copied data as an **incident**: recover and erase it, and log what happened.

    **Marking points:** (i) 1 per weakness; (ii) 1 per requirement or principle correctly applied (1 × 4); (iii) 1 per justified recommendation.

---

## Questions and units

| Question | Units tested |
|---|---|
| 1 | 1, 2, 3, 5, 7, 9, 10, 12 |
| 2 | 4 |
| 3 | 8, 11 (and 1: accountability) |
| 4 | 5, 12 |
| 5 | 10, 6 |
