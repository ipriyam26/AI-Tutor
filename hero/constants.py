INFO_MSG = """I want you to act an expert information collector.
You will help collect all the relevant information from the user, needed to write an essay. You will ask questions to gauge the user's needs and collect information accordingly. You will also give user suggestions on subtopics to select from based on the topic provided by the user.

If you deviate from the conversation casually drive the conversation back to the information collection process. 

If user is confused about some question help them understand it.

If user asks questions that are not relevant to the information collection process, you will respond with "Let's stick to the information collection only".


don't repeat questions
----

Example conversations:

User: I want help with my essay


AI: I can help you with that, I will ask you a few questions and based on your responses we can write an essay together.\nWhat is the topic of the essay?
User: National Parks of US


AI: Lets develop a thesis for this essay. Write a few lines about what you are thinking about National parks of US
User: I want to discuss how important National parks are and I want to focus on national parks of california


AI: Okay, based on your feedback I suggest we also discuss the following topics (a) The protection of animals in National parks (b) prevention of fires in national parks (c ) National parks and campgrounds. Which of these would you like to discuss in your essay?
User: Lets also discuss preventions of fires at National parks


AI: How long do you want the essay to be
User: 1000 words


AI:  Do you want citation and academic sources in your essay(APA or MLA)
User: Yes, MLA


AI: What grade level are you in
User: I'm in High School


AI: Here is the information I have collected for you:

<info>
1. Topic: National Parks of US
2. Word Count: 1000
3. Citation Style: MLA
4. Academic Level: High School
5. Subtopics: Discuss how important National parks are, Focus on national parks of california and preventions of fires at National parks.
</info>

----

Wrap <info></info> tags around the information collected
NEVER assume make up the information, only collect the information that is provided by the user

----
{history}
----


USER:{input}
AI:
"""

THESIS_MSG = """I want you to act an expert thesis writer. given requirements from user, you will write a thesis.
You only need to write a thesis, not the whole essay.
Wrap the thesis with <Thesis> and </Thesis> tags.

Example:

User: Given these requirements, write a thesis
1. Topic: The impact of drugs on society in the USA.
2. Word/Page count: Approximately 600 words.
3. Deadline: The essay needs to be submitted in 2 days.
4. Formatting guidelines: APA style of citation is required.
7. Specific instructions: No specific instructions or requirements provided by your instructor.

AI: <Thesis> While the therapeutic use of drugs plays a critical role in advancing healthcare, the misuse of illicit drugs imposes severe socioeconomic challenges in the USA, manifesting in deteriorated public health, heightened crime rates, and strained economic resources.</Thesis>

----

User: Given these requirements, write a thesis
1. Topic: Food Wastage crisis.
2. Word/Page count: Approximately 1000 words.
3. Deadline: The essay needs to be submitted in 5 days.
4. Formatting guidelines: APA style of citation is required.
7. Specific instructions: No specific instructions or requirements provided by your instructor.

AI: <Thesis> Addressing the pervasive issue of food wastage not only presents an opportunity to combat hunger but also offers a means to mitigate environmental degradation, emphasizing the need for effective strategies for food recovery, redistribution, and public awareness. </Thesis>


----

User: Given these requirements, write a thesis
1. Topic: Rise of AI
2. Word/Page count: Approximately 1500 words.
3. Deadline: The essay needs to be submitted in 5 days.
4. Formatting guidelines: MLA style of citation is required.
7. Specific instructions: No specific instructions or requirements provided by your instructor.

AI: <Thesis> As Artificial Intelligence (AI) rapidly permeates various sectors of society, it simultaneously presents immense potential for economic growth and innovation while invoking complex ethical and societal concerns that necessitate careful navigation and regulation. </Thesis>

----
{history}

----

USER:{input}
AI:
"""

OUTLINE_MSG = """I want you to act an expert outline writer. given a thesis and information about essay, you will write an outline.


Keep in mind that the outline length should corresponding to the word count of the essay. i.e each section will aroung 200-300 words.

Example:

USER: Given this thesis and information, write an outline, of 5 sections.
    Thesis: While the therapeutic use of drugs plays a critical role in advancing healthcare, the misuse of illicit drugs imposes severe socioeconomic challenges in the USA, manifesting in deteriorated public health, heightened crime rates, and strained economic resources.
    Information:
    1. Topic: The impact of drugs on society in the USA.
    2. Word/Page count: Approximately 1000 words.
    4. Formatting guidelines: APA style of citation is required.
    7. Specific instructions: No specific instructions or requirements provided by your instructor.

AI: <Outline>
<document>
<section>
I. Introduction
A. Brief overview of the prevalence of drug use in the USA
B. Thesis statement: "While the therapeutic use of drugs plays a critical role in advancing healthcare, the misuse of illicit drugs imposes severe socioeconomic challenges in the USA, manifesting in deteriorated public health, heightened crime rates, and strained economic resources."
</section>

<section>
II. The Impact of Drug Misuse on Public Health
A. Discussion on the correlation between drug misuse and deteriorating public health
1. Exploration of the mental and physical health effects of drug misuse
2. Discussion on the spread of communicable diseases through drug use, such as HIV/AIDS
B. The financial impact on the healthcare system due to drug-related health issues
</section>

<section>
III. The Relationship Between Drug Misuse and Crime Rates
A. Examination of the link between drug misuse and crime rates
1. Discussion of drug-related crimes (possession, trafficking, etc.)
2. Examination of drug-induced crimes (robbery, assault, etc. caused by need for drugs or under influence)
B. The impact of these crimes on communities and law enforcement
</section>

<section>
IV. The Economic Strain Due to Drug Misuse
A. The financial burden on public resources due to drug-related issues
1. Law enforcement and judiciary costs
2. Healthcare costs
3. Lost workplace productivity
B. Discussion on how this economic strain affects society as a whole
</section>

<section>
V. Conclusion
A. Recap of the societal impacts of drug misuse (public health, crime, and economic strain)
B. Brief discussion on potential strategies to mitigate these impacts
C. Restatement of the thesis and closing thoughts
</section>
</document>
 </Outline>


-----

USER: Given this thesis and information, write an outline, of 6 sections.
    Thesis: As Artificial Intelligence (AI) rapidly permeates various sectors of society, it simultaneously presents immense potential for economic growth and innovation while invoking complex ethical and societal concerns that necessitate careful navigation and regulation."
    Information:
    1. Topic: Rise of AI
    2. Word/Page count: Approximately 1200 words.
    3. Deadline: The essay needs to be submitted in 5 days.
    4. Formatting guidelines: MLA style of citation is required.
    7. Specific instructions: No specific instructions or requirements provided by your instructor.


AI: <Outline>
<document>
<section>
I. Introduction
A. Definition of Artificial Intelligence
B. Brief background of the rise of AI
C. Thesis statement
</section>

<section>
II. The Potential of AI
A. Explanation of how AI drives economic growth
1. Job creation
2. Productivity increase
B. Discussion on the role of AI in innovation
1. Technological advancements
2. Breakthroughs in research and development
3. Personalization and efficiency in various sectors (e.g., healthcare, education)
</section>

<section>
III. Ethical Concerns
A. Data privacy issues
1. Surveillance and data breaches
2. Informed consent in data collection
B. AI and bias
1. Discrimination in AI algorithms
2. Implications for social inequality
</section>

<section>
IV. Societal Concerns
A. Job displacement
1. Automation replacing human labor
2. Required shift in job skills
B. Dependence on technology
1. Impacts on human interaction and society
2. Risk of AI malfunctions or cybersecurity threats
</section>
V. Navigating and Regulating AI
A. Importance of ethical guidelines and legislation
B. Role of education and public awareness
C. Highlight successful examples of AI regulation

<section>
VI. Conclusion
A. Restatement of thesis
B. Brief summary of main points
C. Future outlook on the role of AI in society 
</section>
</document>
</Outline>

----
{history}
-----
USER:{input}
AI:"""

ESSAY_MSG = """I want you to act as an essay writer. You will write the essay in chunks. I will provide you an outline for the chunk. 
You will need to make a  chunk of the essay following the outline chunk provided. 

I need it to have a good amount of perplexity and burstiness.

Keep in mind that what you are writing chunks that will be joined into an essay, so make sure that the chunks are coherent and flow well. Like no random sentences of paragraphs that feel outof place.

{CITATIONS}

Here is a some information that will help all along:
{instruct}

You will need to wrap the chunk with <ESSAY> and </ESSAY> tags.


____

{history}

----
User: Here is the current chunk "{user_input}"
AI:
"""

outline1 = """
<document>

<section>
I. Introduction
A. Brief overview of the prevalence of drug use and abuse in the USA
B. Thesis statement: "The widespread use and abuse of drugs in the United States have far-reaching consequences on society, including detrimental effects on public health, increased crime rates, and significant economic burdens, highlighting the urgent need for comprehensive strategies to address this pressing issue."
</section>

<section>
II. Detrimental Effects on Public Health
A. Discussion on the physical and mental health consequences of drug use and abuse
1. Exploration of the health risks associated with different types of drugs
2. Examination of the impact on individuals, families, and communities
B. The role of drug-related diseases and infections in public health challenges
1. Analysis of the spread of diseases such as HIV/AIDS and hepatitis through drug use
2. Discussion on the burden on healthcare systems and resources
</section>


<section>
III. Increased Crime Rates
A. Examination of the link between drug use and crime rates
1. Discussion of drug-related crimes, such as possession, distribution, and trafficking
2. Analysis of the relationship between drug addiction and criminal behavior
B. The impact of drug-related crimes on communities and law enforcement
1. Discussion on the strain on law enforcement resources and budgets
2. Examination of the social and economic consequences of drug-related crimes
</section>

<section>
IV. Significant Economic Burdens
A. The financial costs of drug use and abuse on society
1. Analysis of the economic impact on healthcare systems and public resources
2. Discussion on the costs of drug-related crimes and incarceration
B. Examination of the indirect economic consequences
1. Analysis of lost productivity and workforce participation due to drug addiction
2. Discussion on the impact on education and human capital development
</section>

<section>
V. Comprehensive Strategies to Address the Issue
A. Importance of prevention and education programs
1. Discussion on the role of schools, communities, and families in prevention efforts
2. Analysis of effective prevention strategies and campaigns
B. The significance of treatment and rehabilitation programs
1. Examination of the importance of access to quality healthcare and addiction treatment services
2. Discussion on the role of support systems and community resources
</section>

<section>
VI. Conclusion
A. Recap of the detrimental effects of drug use and abuse on public health, crime rates, and the economy
B. Emphasis on the urgent need for comprehensive strategies to address the issue
C. Restatement of the thesis and closing thoughts
</section>
</document>
"""
information1 = """
1. Topic: The impact of drugs on society in the USA.
2. Word/Page count: Approximately 600 words.
3. Deadline: The essay needs to be submitted in 2 days.
4. Formatting guidelines: APA style of citation is required.
7. Specific instructions: No specific instructions or requirements provided by your instructor
"""
essay1 = """<ESSAY> Title: The Impact of Drugs on Society in the USA

The United States confronts a critical problem that permeates all strata of society - the prevalent use and abuse of drugs. This pervasive issue brings substantial detrimental impacts on public health, exacerbates crime rates, and imposes extensive economic burdens. Thus, the urgency for comprehensive, strategic approaches to mitigate this widespread problem cannot be overstated.

The adverse effects on public health due to drug abuse are profound and wide-ranging. Drugs of all types, from opioids to stimulants, carry substantial health risks, causing significant damage to both physical and mental well-being (National Institute on Drug Abuse [NIDA], 2021). For instance, consistent drug use can lead to long-term health complications such as heart disease, liver damage, and a range of psychological disorders including depression and anxiety. Such health complications not only detrimentally affect the individuals but also impose a heavy emotional and social burden on families and communities. They endure the pain of seeing their loved ones succumb to addiction, further straining relationships and community bonds.

Additionally, the role of drug use in facilitating the spread of infectious diseases, such as HIV/AIDS and hepatitis, through shared drug paraphernalia is a significant public health challenge (Centers for Disease Control and Prevention [CDC], 2021). These drug-induced health complications pose a considerable burden on the healthcare systems, straining resources that could otherwise be used for other vital health services. This scenario also results in a higher financial cost to the healthcare system due to the increased need for treatment and care for drug-related diseases and infections.

The relationship between drug use and crime is intricately linked and well-documented. Illicit drug use is often associated with a range of criminal activities, from minor offenses like possession and distribution to major crimes such as drug trafficking (Bureau of Justice Statistics [BJS], 2022). Moreover, the desperate conditions brought on by addiction often compel individuals to resort to criminal behavior as a means to sustain their drug habit, leading to a vicious cycle of addiction and crime. The knock-on effect of this is considerable, as neighborhoods become unsafe, instilling fear among residents, and disrupting community life.

Furthermore, drug-related crimes place a significant strain on law enforcement resources, stretching thin their budgets, and diverting attention from other necessary societal protections. The socio-economic consequences of drug-related crimes are, therefore, extensive, affecting not only individuals and families but also communities and society at large.

Examining the issue from an economic standpoint, the financial burden of drug use and abuse on society is immense. The direct costs include the financial strain on healthcare systems due to the increased demand for medical care, and significant public resources expended on law enforcement and incarceration for drug-related crimes (Office of National Drug Control Policy [ONDCP], 2022). However, the indirect economic implications are equally severe. Productivity losses due to drug addiction, which can result in absenteeism, job losses, or reduced employability, contribute to the economic drain. The impact on education and human capital development is also significant, as drug abuse can stymie academic progress and hinder cognitive development, leading to a less skilled and less productive workforce in the long run.

To combat this multi-dimensional problem, a comprehensive approach encompassing prevention, treatment, and rehabilitation is needed. Prevention and education programs play a crucial role in informing individuals, especially young people, about the perils of drug use. Schools, communities, and families need to work hand in hand in these prevention efforts, fostering an environment that discourages drug use and promotes healthier alternatives (NIDA, 2022).

Equally important is ensuring access to quality healthcare and addiction treatment services for those grappling with drug abuse. Robust rehabilitation programs, coupled with supportive environments and community resources, can guide individuals towards recovery, reduce
 </ESSAY>

<CITATIONS>
References:
Bureau of Justice Statistics. (2022). Drugs and Crime.
Centers for Disease Control and Prevention. (2021). Drug Overdose.
Centers for Disease Control and Prevention. (2022). Substance Use and Mental Health.
National Institute on Drug Abuse. (2021). Understanding Drug Use and Addiction.
National Institute on Drug Abuse. (2022). Preventing Drug Use among Children and Adolescents.
Office of National Drug Control Policy. (2022). The Economic Impact of Illicit Drug Use on American Society. 
</CITATIONS>"""


outline2 = """

<document>

<section>
I. Introduction
A. Definition of Artificial Intelligence
B. Brief background of the rise of AI
C. Thesis statement
</section>

<section>
II. The Potential of AI
A. Explanation of how AI drives economic growth
1. Job creation
2. Productivity increase
B. Discussion on the role of AI in innovation
1. Technological advancements
2. Breakthroughs in research and development
3. Personalization and efficiency in various sectors (e.g., healthcare, education)
</section>

<section>
III. Ethical Concerns
A. Data privacy issues
1. Surveillance and data breaches
2. Informed consent in data collection
B. AI and bias
1. Discrimination in AI algorithms
2. Implications for social inequality
</section>


<section>
IV. Societal Concerns
A. Job displacement
1. Automation replacing human labor
2. Required shift in job skills
B. Dependence on technology
1. Impacts on human interaction and society
2. Risk of AI malfunctions or cybersecurity threats
</section>

<section>
V. Navigating and Regulating AI
A. Importance of ethical guidelines and legislation
B. Role of education and public awareness
C. Highlight successful examples of AI regulation
</section>

<section>
VI. Conclusion
A. Restatement of thesis
B. Brief summary of main points
C. Future outlook on the role of AI in society
</section>

</document>
"""
information2 = """
    1. Topic: Rise of AI
    2. Word/Page count: Approximately 1000 words.
    3. Deadline: The essay needs to be submitted in 5 days.
    4. Formatting guidelines: MLA style of citation is required.
    7. Specific instructions: No specific instructions or requirements provided by your instructor.
"""
essay2 = """<ESSAY>Title: Rise of AI

Artificial Intelligence (AI) refers to the simulation of human intelligence in machines, specifically computer systems, programmed to mimic human thoughts and actions. The rise of AI in the modern era is nothing short of revolutionary. This technological marvel is rapidly embedding itself in various facets of society. While it presents immense potential for economic growth and innovation, it simultaneously raises complex ethical and societal concerns that necessitate careful navigation and regulation.

The potential of AI as a catalyst for economic growth is remarkable. It is not just about robots replacing human jobs; rather, it's about the creation of new opportunities and roles. Experts estimate that AI has the potential to create a net increase of 12 million jobs globally by 2025 (World Economic Forum, 2021). These jobs range from designing and implementing AI systems to their maintenance, oversight, and ethical management. Moreover, AI is becoming the powerhouse of productivity. It can streamline processes, automate routine tasks, and increase efficiency, allowing humans to focus on more complex, creative, and emotionally driven endeavors.

AI is at the heart of contemporary innovation, fostering advancements that were once considered the realm of science fiction. Autonomous vehicles, AI-driven predictive analytics, smart homes, and even AI-assisted scientific discoveries are all testament to the relentless technological advancement propelled by AI. Furthermore, AI has revolutionized research and development across various sectors. It facilitates the analysis of large datasets, enabling groundbreaking findings in diverse fields like genomics, climate science, and social sciences. Notably, AI's transformative power is also driving unprecedented personalization and efficiency in critical sectors like healthcare and education. From AI-powered personalized learning tools that adapt to a student's learning style to predictive diagnostics in healthcare that enable early intervention, the applications are profoundly altering our lives.

Despite these opportunities, the rise of AI is not without significant ethical concerns. Data privacy remains a fundamental issue. As AI systems feed on massive data, concerns around surveillance, potential data breaches, and the complexities of obtaining informed consent for data collection are growing (Harvard Business Review, 2022). This era of 'big data' thus requires stringent data protection measures to ensure users' privacy. Bias in AI is another critical ethical issue. AI systems learn from the data they are fed, and if these datasets contain biases, the AI algorithms can inadvertently perpetuate and amplify these biases, leading to discriminatory outcomes. These issues have significant implications for social equality and justice.

Societal concerns around AI are equally pressing. There's a growing fear of job displacement due to AI-driven automation. The McKinsey Global Institute (2022) suggests that while new jobs are likely to be created, a significant shift in skills would be required, emphasizing the need for ongoing education and retraining initiatives. Moreover, as society becomes increasingly dependent on technology, concerns around the over-reliance on AI systems arise. This dependence could drastically alter human interactions and presents risks in the face of potential AI malfunctions or cybersecurity threats.

Given these complex challenges, the need to navigate and regulate the rise of AI responsibly is clear. Ethical guidelines and robust legislative frameworks are crucial to govern the development and application of AI. Such measures can ensure that AI technology respects privacy, promotes fairness, and operates within socially acceptable boundaries. The importance of public awareness and education around AI cannot be overstated. Knowledge of the benefits and risks associated with AI is essential for informed public discourse and decision-making. Certain jurisdictions, like the European Union with its draft Artificial Intelligence Act, provide shining examples of how proactive regulation can work to manage AI (European Commission, 2021).

In conclusion, as we navigate the rising tide of AI in society, we are faced with a landscape of both promise and challenge. AI's potential to drive economic growth and foster innovation is astounding, yet

 it raises urgent ethical and societal concerns. It's a terrain that demands careful regulation, widespread education, and a vigilant society. The role of AI in our future will be defined by our ability to maximize its benefits while responsibly mitigating its risks.
</ESSAY>

<CITATIONS>
Works Cited

European Commission. (2021). "Proposal for a Regulation Laying Down Harmonised Rules on Artificial Intelligence." EUR-Lex.

Harvard Business Review. (2022). "AI and Privacy: Balancing Benefits and Risks." HBR.org.

McKinsey Global Institute. (2022). "The Future of Work in the Age of AI." McKinsey.com.

World Economic Forum. (2021). "AI and the Future of Jobs." weforum.org.
</CITATIONS>

"""

EXAMPLES = [
    {
        "input": f"Information\n{information1}\nOutline{outline1}",
        "output": f"Essay\n{essay1}",
    },
    {
        "input": f"Information\n{information2}\nOutline{outline2}",
        "output": f"Essay\n{essay2}",
    },
]


examples = [
    {
        "input": """I. Introduction
A. Engaging hook to capture the reader's attention
B. Brief overview of the current state of the medical industry
C. Thesis statement: "Through its extensive influence over the medical industry and government decisions, big pharma exerts immense control over the world, raising serious concerns about the integrity of healthcare systems, the well-being of patients, and the global implications of prioritizing profit over public health.""",
        "output": """
<ESSAY>
Have you ever pondered why the cost of prescription drugs continues to escalate, despite the relatively stable manufacturing expenses? Have you questioned why certain medications, potentially laced with harmful side effects, are aggressively advertised? The answer to these quandaries resides in the colossal influence exerted by 'big pharma' - the mighty pharmaceutical titans that command the medical industry.

The medical field is pivotal to our society, responsible for offering indispensable healthcare facilities and generating life-saving medications. Nevertheless, the character of this industry has drastically evolved over time. The era where doctors were singularly focused on their patient's welfare and care has given way to a new age. The contemporary medical industry is primarily a profit-centered apparatus, with pharmaceutical corporations at the forefront.

In recent years, the authority brandished by big pharma has reached unmatched heights, granting them the power to mold healthcare policies, monopolize medication markets, and sway medical research. This domination jeopardizes not only the reliability of healthcare systems but also significantly threatens patient well-being. Moreover, the global ramifications of prioritizing revenue over public health are extensive, perpetuating health disparities and impeding access to cost-effective medicines on a worldwide scale.

Bearing this in mind, it is of paramount importance to investigate the strategies by which big pharma governs the world. We need to scrutinize specific instances where their influence has left an indelible imprint. By comprehending the mechanisms they employ to enforce control, we can start addressing the core issues. It is through this understanding that we can strive for a more transparent and patient-oriented medical industry. </ESSAY>
""",
    },
    {
        "input": """II. Evolution of the Medical Industry
A. Historical background of the medical industry
1. Introduction of pharmaceutical companies
2. Shift towards profit-driven healthcare
B. Discussion on the current state of the medical industry
1. Dominance of pharmaceutical giants
2. Increasing costs of medications and healthcare services""",
        "output": """<ESSAY> The medical industry has borne witness to remarkable transformations throughout history. During its infancy, healthcare was chiefly supplied by independent practitioners and small community clinics. However, the emergence of pharmaceutical companies in the late 19th century signaled a pivotal moment. These entities ushered in advancements in medical research and the creation of life-saving drugs, revolutionizing the medical field. Although these developments initially had a positive impact on healthcare, they also set the stage for the current profit-driven healthcare system.

In the modern medical landscape, pharmaceutical titans exert substantial power and sway. With their enormous financial resources and comprehensive research abilities, these companies have ascended to be the driving forces behind medical advancements. They maintain market domination and command the production, distribution, and pricing of medications. This control allows them to dictate the trajectory of medical research and innovation, often prioritizing high-profit drugs over those catering to critical health needs.

However, a troubling facet of the current state of the medical industry is the soaring costs of medications and healthcare services. Pharmaceutical corporations possess the power to fix prices for their drugs, often imposing exorbitant charges for life-saving treatments. This practice can inflict devastating effects on patients who can't afford the necessary medicines, leading to compromised health outcomes, and in extreme cases, death.

Moreover, the escalating expenses of healthcare services, encompassing everything from hospital stays to diagnostic tests, place a considerable strain on individuals and the overall healthcare system. This shift towards a profit-driven healthcare model has birthed a system where financial gain supersedes patient well-being, leaving many without the care they so desperately require. </ESSAY>  """,
    },
    {
        "input": """III. Control and Influence of Big Pharma
A. Exploration of the strategies used by big pharma to control the industry
1. Drug pricing and monopolies
2. Lobbying and political influence
B. Examination of the influence of big pharma on government decisions
1. Campaign contributions and influence on legislators
2. Revolving door between pharmaceutical industry and government positions""",
        "output": """<ESSAY>
    One of the primary methods that big pharma employs to dominate the medical industry is through drug pricing and establishing monopolies. These pharmaceutical giants wield the power to assign prices for their drugs, often setting astronomical charges for life-saving treatments. By monopolizing the market, they extinguish competition and establish a dominant hold on the supply and distribution of medications. This strategy allows them to maximize their profits and retain control over the industry.

Yet another potent weapon at the disposal of big pharma is their capacity to lobby and exert political influence. Every year, these companies invest millions into lobbying efforts, manipulating lawmakers, and molding healthcare policies to their benefit. Through generous campaign contributions and relentless lobbying, they gain access to key decision-makers and can tilt legislative scales in their favor. This influence over policymakers empowers them to safeguard their interests, preserve their dominance, and further cement their control over the medical industry.

One of the most noteworthy ways in which big pharma exerts influence on government decisions is through hefty campaign contributions to political candidates. By injecting substantial funds into election campaigns, these pharmaceutical behemoths win favor with legislators who then tend to support policies in line with their interests. This financial clout enables big pharma to sculpt the political landscape, ensuring their voice resonates in discussions pertaining to healthcare legislation and regulations.

Another disconcerting aspect of big pharma's influence on government decisions is the revolving door between the pharmaceutical industry and governmental roles. Numerous individuals in influential government positions have ties to the pharmaceutical industry, either through past employment or prospective career opportunities. This poses a conflict of interest and raises queries about the neutrality of decision-making procedures. This close association between the pharmaceutical industry and government officials further fortifies big pharma's control over the medical industry, compromising the integrity of healthcare systems. </ESSAY>""",
    },
    {
        "input": """IV. Instances of Big Pharma's Impact
A. Case study: Opioid crisis in the United States
1. Role of pharmaceutical companies in promoting and misleading information about opioids
2. Consequences on public health and well-being
B. Discussion on other specific instances of big pharma's control and impact
1. Influence on drug approval and regulation processes
2. Manipulation of clinical trial data""",
        "output": """
<ESSAY> A glaring instance of big pharma's control and its impact on public health is embodied in the opioid crisis that has gripped the United States. Pharmaceutical companies had a significant role in promoting and disseminating misleading information about opioids, which led to rampant overprescribing and a subsequent addiction epidemic. These corporations aggressively marketed opioids as safe and effective solutions for pain management, trivializing their addictive nature and downplaying the risks associated with long-term use. Through their influence, they managed to convince healthcare providers to prescribe opioids more liberally, eventually contributing to a widespread addiction and overdose crisis.

The repercussions of the opioid epidemic on public health and well-being have been catastrophic. The United States has witnessed a steep surge in opioid-related deaths and addiction rates, causing havoc in families and communities. The rampant overprescribing of opioids has not only led to addiction but also served as a gateway to heroin usage for many individuals. The economic toll of the crisis is substantial, marked by ballooning healthcare costs and loss of productivity. The pharmaceutical corporations implicated in promoting opioids have been the target of multiple lawsuits and settlements, underscoring the serious ramifications of their actions on public health.

Moreover, big pharma's influence stretches to the realms of drug approval and regulatory processes, enabling them to prioritize profits over safety and efficacy. Pharmaceutical companies often apply pressure on regulatory agencies, advocating for quickened approvals and relaxed safety standards. This undermines the integrity of the drug approval process, as medications may gain approval without adequate testing or a thorough assessment of potential risks. The influence of big pharma in this context raises concerns about the safety and efficacy of drugs available on the market, potentially exposing patients to unnecessary risks.

Another manifestation of big pharma's control and influence is seen in the manipulation of clinical trial data. There have been instances where pharmaceutical corporations selectively report or skew trial results to favor their products. By suppressing negative data or overstating positive outcomes, they can foster a misleading perception of a drug's effectiveness and safety. This manipulation not only compromises the scientific integrity of clinical trials but also endangers patients by offering inaccurate information. Big pharma's influence in shaping the narrative surrounding their medications impedes transparency and hinders informed decision-making.</ESSAY>
""",
    },
    {
        "input": """V. Global Implications of Big Pharma's Influence
A. Discussion on the global reach of pharmaceutical giants
1. Exploitation of developing countries
2. Impacts on access to essential medications
B. Exploration of the ethical and moral concerns raised by big pharma's global influence
1. Prioritization of profit over public health
2. Limited research on neglected diseases""",
        "output": """<ESSAY>The influence of big pharma doesn't stop at national borders. It has a far-reaching impact that transcends geographical boundaries, significantly affecting developing countries. Pharmaceutical giants often exploit the weaknesses of these nations, leveraging their weak regulations and limited resources. They engage in practices like patent abuse and price gouging, rendering essential medications unaffordable for many people in these countries. Such exploitation sustains health inequalities and impedes access to life-saving treatments.

Another key global implication of big pharma's influence lies in its impact on access to essential medications. These pharmaceutical behemoths often prioritize profits over public health, setting high drug prices that are prohibitive for many individuals, both globally and domestically. This inaccessibility to vital medications can lead to dire consequences, especially for those living in low-income countries or marginalized communities. The control exercised by big pharma thwarts the efforts to achieve universal healthcare, thereby perpetuating health disparities on a global scale.

The vast global influence of big pharma gives rise to serious ethical and moral concerns, largely due to their practice of prioritizing profits over public health. The actions of these pharmaceutical giants reflect a blatant disregard for patient well-being and the integrity of healthcare systems. By setting exorbitant prices for life-saving medications and partaking in exploitative practices, they contribute to sustaining health inequalities and obstruct access to critical treatments. This profit-centric approach challenges the fundamental principles of healthcare and brings into question the ethical values of these corporations.

Adding to the list of ethical concerns triggered by big pharma's global influence is the limited research and development dedicated to neglected diseases. Pharmaceutical companies often channel their resources towards drugs promising high profitability, often overlooking diseases that predominantly affect low-income countries. This lack of investment widens the gaps in healthcare, with marginalized populations denied access to treatments for diseases that disproportionately impact them. The global implications of this neglect are substantial as neglected diseases continue to afflict and claim lives among vulnerable populations.

In conclusion, the far-reaching global implications of big pharma's influence trigger significant ethical and moral concerns. Their exploitation of developing countries and impacts on access to essential medications further entrench health inequalities on a worldwide scale. The prioritization of profit over public health undermines the integrity of healthcare systems and hampers efforts to achieve universal healthcare. Moreover, the limited research dedicated to neglected diseases exacerbates health disparities and denies marginalized populations access to life-saving treatments. Addressing these global implications and working towards a more equitable and patient-centric medical industry is an imperative need of the hour.</ESSAY>
""",
    },
    {
        "input": """VI. Conclusion
A. Summary of main points discussed
B. Restatement of thesis
C. Call to action for reforms in the medical industry and government policies""",
        "output": """<ESSAY>
Throughout this exploration, we have delved into the multifaceted ways big pharma maintains its dominance over the global healthcare landscape, sparking profound concerns about the sanctity of healthcare systems, patient well-being, and the worldwide implications of valuing profit over public health. The evolution of the medical industry was explored, underscoring the rise of pharmaceutical giants and the escalating costs of medications and healthcare services. We also illuminated the strategies deployed by big pharma to hold sway over the industry, including establishing monopolies and driving drug pricing, along with their potent influence on governmental decisions through lobbying and the revolving-door phenomenon between the pharmaceutical industry and government positions. 

Furthermore, we delved into specific instances where big pharma's dominion has had tangible impacts, such as their role in the opioid crisis in the United States and their sway over drug approval and regulation processes. Lastly, we navigated the global implications of big pharma's influence, pointing to the exploitation of developing nations, the impact on access to essential medications, and the moral and ethical concerns spurred by their actions, particularly their preference for profit over public health and inadequate focus on neglected diseases.

In conclusion, big pharma wields considerable power and control on a global scale through its overwhelming influence over the medical industry and governmental decisions. This dominance stirs significant concerns about the integrity of healthcare systems, patient welfare, and the international implications of prioritizing profit over public health. The authority commanded by pharmaceutical behemoths endangers the accessibility and affordability of essential medications, propagates health inequalities, and stifles efforts towards achieving universal healthcare.

To tackle the problems spotlighted in this discussion, it's imperative to push for reforms in the medical industry and governmental policies. Placing public health over profit should be paramount in all decision-making processes. This can be accomplished by promoting greater transparency and accountability in drug pricing, ensuring that essential medications are affordable and accessible to everyone. 

Moreover, stricter regulations are needed to curb the influence of big pharma in the political arena, encompassing campaign finance reforms and constraints on the revolving door between the pharmaceutical industry and governmental roles. Further, increased investment in research and development for neglected diseases is crucial to ensure that all individuals have access to life-saving treatments, irrespective of their socioeconomic standing or geographic location.

By driving these reforms, we can aim for a medical industry that prioritizes patients, transparency, and equity. It's vital to prioritize public health over profit and ensure that healthcare systems serve the interests of individuals rather than the financial ambitions of pharmaceutical giants. Only through such collective endeavors can we start dismantling big pharma's control and establish a healthcare system that genuinely prioritizes the welfare of patients worldwide.
</ESSAY>""",
    },
]


AI_FIX = """When it comes to writing content, two factors are crucial, “perplexity” and “burstiness.” Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness.

Help me rewrite the following content to have more perplexity and burstiness. You can add, remove, or change words. You can also change the order of the sentences. You can also change the order of the words in the
Keep in mind if the essay contains citation's please try to keep them.
Respect the minimum {word_count} word count of the essay.

Content: {content}
"""

