# Mock exam 2

<div class="exam-header" markdown>

**CSC 583: Computer and Information Security — Mock examination 2**

**Time allowed:** 2½ hours

**Instructions:** Answer **Question 1** and any other **THREE** questions. Each question carries **20 marks**.

*This paper follows the format assumed on the [exam technique](exam-technique.md#the-paper) page, with four answers instead of three. The real paper's instructions may differ.*

</div>

Sit this one after [Mock exam 1](mock-exam-1.md). It deliberately uses different topics, so between them the two papers cover all twelve units. The table at the end shows which unit each question tests.

---

## Question 1 (compulsory)

**1a.** State the three categories of attack surface. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Network attack surface; software attack surface; human attack surface. ([Unit 2](../unit-2-attacks.md#categories-of-attack-surface))

    **Marking points:** all three (2); any two (1).

**1b.** State the three types of public key (digital) certificate. <span class="marks">(2 marks)</span>

??? success "Model answer"
    TLS/SSL certificate; code signing certificate; client certificate. ([Unit 4](../unit-4-cryptography.md#digital-certificates))

    **Marking points:** all three (2); any two (1).

**1c.** Name the four generations of firewall, in order. <span class="marks">(2 marks)</span>

??? success "Model answer"
    1. Stateless (packet-filtering) firewalls.
    2. Stateful firewalls.
    3. Application-level gateways (proxy firewalls).
    4. Next-generation firewalls (NGFW).

    ([Unit 5](../unit-5-firewalls.md#firewall-evolution-the-four-generations))

    **Marking points:** ½ per generation in the right order.

**1d.** State the two modes of WPA and what each is for. <span class="marks">(2 marks)</span>

??? success "Model answer"
    - **WPA-Personal:** for home use.
    - **WPA-Enterprise:** for organisations, authenticating users through a RADIUS server.

    ([Unit 7](../unit-7-wireless-mobile.md#each-protocol-in-detail))

    **Marking points:** 1 per mode with its use.

**1e.** Define *network access control (NAC)* and name its two types. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Network access control, also known as network admission control, is the process of restricting unauthorized users and devices from gaining access to a corporate or private network. Its two types are **pre-admission** and **post-admission** NAC. ([Unit 8](../unit-8-access-control.md#network-access-control-nac))

    **Marking points:** definition (1); both types (1).

**1f.** Define *ransomware*. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Ransomware is malware that encrypts files or locks users out of their systems, demanding a ransom for decryption or access restoration; non-payment leads to data loss and disruption. ([Unit 9](../unit-9-malware.md#ransomware))

    **Marking points:** encrypts files or locks users out (1); demands a ransom for restoration (1).

**1g.** Name four common database security threats. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Any four of: SQL injection; insider threats (users with excessive privileges); password sharing; misconfigured database software; unpatched vulnerabilities; unmonitored database activity. ([Unit 11](../unit-11-database-security.md#common-database-security-threats))

    **Marking points:** ½ per threat.

**1h.** List the four typical components of an IDPS solution. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Sensor or agent; management server; database server; console. ([Unit 12](../unit-12-idps.md#idps-components))

    **Marking points:** ½ per component.

**1i.** Explain the design principle of *least privilege*. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Least privilege means every process and every user of the system should operate using the **least set of privileges necessary to perform the task**. A good example of its use is role-based access control. ([Unit 1](../unit-1-security-concepts.md#least-privilege))

    **Marking points:** meaning (1); example (1).

**1j.** Name the five legal issues in information security covered in the course. <span class="marks">(2 marks)</span>

??? success "Model answer"
    Unauthorized access; data protection and privacy laws; cybercrime; copyright and software licensing; electronic fraud. ([Unit 10](../unit-10-ethics-legal.md#legal-issues-in-information-security))

    **Marking points:** all five (2); three or four (1).

---

## Question 2

**2a.** List **ten** of the seventeen essential security practices. <span class="marks">(5 marks)</span>

??? success "Model answer"
    Any ten of the seventeen:

    1. access control;
    2. awareness and training;
    3. audit and accountability;
    4. certification, accreditation, and security assessments;
    5. configuration management;
    6. contingency planning;
    7. identification and authentication;
    8. incident response;
    9. maintenance;
    10. media protection;
    11. physical and environmental protection;
    12. planning;
    13. personnel security;
    14. risk assessment;
    15. systems and services acquisition;
    16. system and communications protection;
    17. system and information integrity.

    ([Unit 1](../unit-1-security-concepts.md#essential-security-practices))

    **Marking points:** ½ per practice (½ × 10).

**2b.** Explain the following fundamental security design principles: economy of mechanism, fail-safe defaults, complete mediation and separation of privilege. <span class="marks">(8 marks)</span>

??? success "Model answer"
    - **Economy of mechanism:** the design of security measures in both hardware and software should be **as simple and small as possible**, because a simple, small design is easier to test and verify thoroughly.
    - **Fail-safe defaults:** access decisions should be based on **permission rather than exclusion**. The default situation is lack of access, and the protection scheme identifies the conditions under which access is permitted.
    - **Complete mediation:** **every access must be checked** against the access control mechanism. Systems should not rely on access decisions retrieved from a cache.
    - **Separation of privilege:** **multiple privilege attributes** are required to reach a restricted resource; multifactor user authentication is a good example. It also means moving high-privilege operations into a separate process, so day-to-day work runs with lower privileges.

    ([Unit 1](../unit-1-security-concepts.md#fundamental-security-design-principles))

    **Marking points:** 2 per principle: meaning (1), reason or example (1).

**2c.** At a state ministry in Enugu, an audit reports that:

- the staff portal grants every new account full access until an administrator removes rights;
- after a user logs in once, the system remembers the permission decision for the whole week without checking again;
- administrators do their daily email and browsing with their administrator accounts.

For each finding, name the design principle being broken, and recommend a fix. <span class="marks">(7 marks)</span>

??? success "Model answer"
    1. **Full access until rights are removed → breaks *fail-safe defaults*.**
        - **Fix:** new accounts start with **no access**, and rights are granted explicitly (default deny).
        - **Why:** if an administrator forgets a step, the result is a lack of access, not an exposure.
    2. **Cached permission for a week → breaks *complete mediation*.**
        - **Fix:** check every access against the access control mechanism.
        - **Why:** if rights are revoked on Monday, a cached decision would still let the user in until the week ends. *(2 marks)*
    3. **Administrators browsing as administrators → breaks *least privilege*, and *separation of privilege* in its second sense.**
        - **Fix:** each administrator uses a normal account for day-to-day work and switches to the privileged account only for administrative tasks.
        - **Why:** malware picked up while browsing then runs with low privileges and can't take over the system. *(3 marks)*

    **Marking points:** each principle named (1 × 3); each fix with reasoning (1 + 1 + 1), plus 1 for linking finding 3 to both principles.

---

## Question 3

**3a.** Explain the following active attacks: masquerade, replay, modification of messages, and denial of service. <span class="marks">(8 marks)</span>

??? success "Model answer"
    - **Masquerade:** the attacker pretends to be an authorized user of a system, in order to gain access or to gain greater privileges than they are authorized for.
    - **Replay:** a valid data transmission is maliciously or fraudulently **repeated or delayed**, either by the originator or by an adversary who intercepts the data and retransmits it.
    - **Modification of messages:** the attacker **removes** a message from the network traffic, **alters** it, and **reinserts** it.
    - **Denial of service (DoS):** a user or organisation is deprived of the services of a resource they would normally expect to have. In a **distributed** DoS (DDoS), large numbers of compromised systems attack a single target.

    ([Unit 2](../unit-2-attacks.md#active-attacks))

    **Marking points:** 2 per attack: explanation (1) plus the key detail in bold (1).

**3b.** State the two points the courseware gives for each of the following OS security measures: regular updates and patching, strong authentication, access control, and secure configuration. <span class="marks">(4 marks)</span>

??? success "Model answer"
    - **Regular updates and patching:** keep the OS and all software up to date with the latest security patches; enable automatic updates.
    - **Strong authentication:** use multi-factor authentication (MFA); enforce strong password policies, including complexity requirements and regular password changes.
    - **Access control:** implement the principle of least privilege (PoLP); use role-based access control (RBAC) to manage permissions.
    - **Secure configuration:** harden the OS by disabling unnecessary features and services; follow security benchmarks such as those from the Center for Internet Security (CIS) and ISO 27001.

    ([Unit 3](../unit-3-os-security.md#security-measures-to-protect-operating-systems))

    **Marking points:** ½ per point (½ × 8).

**3c.** A courier company in Kano reports three incidents:

- a former employee logs in with a colleague's stolen password and approves refunds to his own account;
- a captured "payment approved" message is sent to the server again an hour later, and a second payment is made;
- the company's tracking website is flooded with traffic from thousands of infected home computers and stops responding.

Classify each incident as one of the active attacks, and recommend one OS security measure or courseware control against each. Justify your answers. <span class="marks">(8 marks)</span>

??? success "Model answer"
    1. **Stolen password → masquerade.**
        - **Why:** he pretends to be an authorized user to gain access.
        - **Control:** *strong authentication* with MFA. A password alone is then not enough, which is the separation-of-privilege idea ([Unit 3](../unit-3-os-security.md#security-measures-to-protect-operating-systems)).
    2. **Re-sent approval message → replay.**
        - **Why:** a valid transmission is fraudulently repeated.
        - **Control:** protect the messages cryptographically (e.g. over TLS, with unique, time-limited transaction values), so a repeated message is rejected ([Unit 4](../unit-4-cryptography.md#cryptographic-protocols-tls-ssl-and-ssh)). It is not modification: the message was not altered, only repeated.
    3. **Flood from infected home computers → distributed denial of service (DDoS).**
        - **Why:** many compromised systems deprive users of the service. The infected machines form a **botnet** ([Unit 9](../unit-9-malware.md#botnets)).
        - **Control:** *firewalls and network security*, with traffic filtering and extra capacity, plus *IDPS* to detect and respond in real time.

    **Marking points:** each attack classified with its reason (1½ × 3 = 4½); each justified control (1 × 3); naming the botnet (½).

---

## Question 4

**4a.** Compare WPA2 and WPA3 in terms of release year, encryption, improvements and drawbacks. <span class="marks">(8 marks)</span>

??? success "Model answer"
    | Criterion | WPA2 | WPA3 |
    |---|---|---|
    | **Release year (2)** | 2004 | 2018 |
    | **Encryption (2)** | AES (AES-CCMP) | Enhanced encryption: CCMP or GCMP as the authenticated encryption protocol |
    | **Improvements (2)** | Over WPA: better administration and lower vulnerability; became the industry standard | Enhanced encryption; improved protection against dictionary brute force attacks; simplified device configuration via Wi-Fi Easy Connect |
    | **Drawbacks (2)** | Vulnerable to the key reinstallation attack (KRACK); difficulties in enterprise settings; older equipment may need upgrades | Deployment complexity; low user adoption; compatibility issues with older devices and equipment |

    ([Unit 7](../unit-7-wireless-mobile.md#each-protocol-in-detail))

    **Marking points:** 1 per cell (1 × 8).

**4b.** Name the two protocols that make up TLS, and list and explain the six steps of the SSL handshake. <span class="marks">(7 marks)</span>

??? success "Model answer"
    **TLS** consists of the **Handshake Protocol**, which establishes a secure connection and authenticates the server using public key cryptography, and the **Record Protocol**, which secures the data sent during the connection using the negotiated cipher suite and keys.

    The SSL handshake:

    1. **Client Hello:** the client sends the SSL versions, cipher suites and other parameters it supports.
    2. **Server Hello:** the server replies with its chosen SSL version and cipher suite, and a digital certificate if required.
    3. **Key Exchange:** client and server exchange cryptographic parameters to establish a shared secret key.
    4. **Authentication:** the client verifies the server's digital certificate (and optionally the reverse).
    5. **Session Key Generation:** both parties generate session keys from the exchanged parameters.
    6. **Secure Communication:** both use the session keys to encrypt and decrypt the data sent during the session.

    ([Unit 4: TLS](../unit-4-cryptography.md#transport-layer-security-tls), [SSL](../unit-4-cryptography.md#secure-sockets-layer-ssl))

    **Marking points:** both TLS protocols (1); 1 per handshake step (1 × 6).

**4c.** A café in Port Harcourt offers free Wi-Fi protected by WEP, with the router's default admin password unchanged. Customers use it to log in to their bank's website. Explain the risks and recommend improvements, with justification. <span class="marks">(5 marks)</span>

??? success "Model answer"
    **Risks:**

    - **WEP is obsolete:** it uses the insecure RC4 cipher and shared key authentication and has been widely exploited, so an attacker nearby can read or tamper with traffic. That is eavesdropping, a passive attack, or modification, an active one.
    - **The default admin password:** anyone can reconfigure the router, for example to redirect customers to fake sites (a man-in-the-middle).

    **Recommendations:**

    - Switch to **WPA3** (or WPA2 at least) with a strong passphrase.
    - Change the **administrative password**, update the **firmware** and disable **unnecessary services**. These are among the six wireless security measures ([Unit 7](../unit-7-wireless-mobile.md#why-wireless-networks-are-exposed-and-the-six-security-measures)).
    - Customers should use only **HTTPS (TLS)** sites, so that their banking data stays encrypted even on an untrusted network.

    **Marking points:** WEP risk (1); default password risk (1); WPA3/WPA2 recommendation with reason (1); router hardening (1); HTTPS/TLS advice (1).

---

## Question 5

**5a.** Define each of the following types of malware: Trojan horse, spyware, rootkit and keylogger. <span class="marks">(8 marks)</span>

??? success "Model answer"
    - **Trojan horse:** malware that disguises itself as legitimate software to trick users into installing it, then delivers malicious payloads such as backdoor access or data theft.
    - **Spyware:** malware specifically designed to secretly monitor user activity and collect personal information, which it sends to attackers for purposes such as identity theft.
    - **Rootkit:** provides unauthorized access to a system and hides its presence by modifying system files, which makes it difficult to detect and enables control of the system.
    - **Keylogger:** records keystrokes to capture sensitive information such as passwords and credit card numbers. IT administrators sometimes use keyloggers legitimately, but cybercriminals often use them for identity theft.

    ([Unit 9](../unit-9-malware.md#malware-types-that-threaten-pc-and-enterprise-systems))

    **Marking points:** 2 per type: what it is (1) and its distinctive behaviour (1).

**5b.** State and explain the three groups of response techniques an IPS uses, with an example of each. <span class="marks">(6 marks)</span>

??? success "Model answer"
    IPS technologies differ from IDS technologies by one characteristic: they can respond to a detected threat by trying to prevent it from succeeding.

    - **The IPS stops the attack itself:** e.g. it terminates the network connection used for the attack, or blocks access to the target from the offending user account or IP address.
    - **The IPS changes the security environment:** it changes the configuration of other security controls, e.g. it reconfigures a network firewall to block access from the attacker, or alters a host-based firewall on the target.
    - **The IPS changes the attack's content:** it removes or replaces the malicious parts of an attack to make it benign, e.g. it removes an infected attachment from an email and then lets the cleaned email through.

    ([Unit 12](../unit-12-idps.md#how-an-ips-responds-three-groups-of-response-techniques))

    **Marking points:** 2 per group: explanation (1) and example (1).

**5c.** At a Lagos law firm, a staff member installed a free "PDF converter" from an email link. Since then, the office's files have not changed and no warning has appeared, but a client's online banking password was used by someone else two days after she typed it on that PC. Identify the most likely malware types, and recommend a response using the malware protection stages. <span class="marks">(6 marks)</span>

??? success "Model answer"
    **Identify.**

    - **Trojan horse:** it was disguised as legitimate software (the "PDF converter") and installed by the user.
    - **Keylogger** (or a spyware or infostealer payload): it secretly captured a password as it was typed.
    - **Not ransomware:** the files have not been encrypted and no ransom demand appeared.

    **Respond** ([Unit 9](../unit-9-malware.md#the-three-malware-protection-stages)):

    - **Post-execution response:** isolate the endpoint, terminate the malicious process, quarantine the file and roll back its changes. Then change every password typed on that PC from a clean device, and warn the client.
    - **Runtime detection:** deploy behavioural analysis (e.g. EDR) so that hidden data-stealing activity is caught next time.
    - **Pre-execution detection:** keep signature-based antivirus updated, and train staff on email attachments and downloads (a malware protection best practice).

    **Marking points:** Trojan with reason (1); keylogger or spyware with reason (1); ruling out ransomware (1); each stage applied (1 × 3).

---

## Questions and units

| Question | Units tested |
|---|---|
| 1 | 1, 2, 4, 5, 7, 8, 9, 10, 11, 12 |
| 2 | 1 |
| 3 | 2, 3 (and 4, 9) |
| 4 | 7, 4 (and 2) |
| 5 | 9, 12 |

Unit 6 (information security policy) is tested in [Mock exam 1](mock-exam-1.md), Question 5.
