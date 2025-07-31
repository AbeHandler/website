---
layout: post
title:  'How do you make a "theoretical contribution" in business research?' 
date:   2025-03-11 12:00:53-0400
categories: MISQ
---

How do you make a "theoretical contribution" in business research? One way to answer that question is by studying how business researchers are trained. Learning how reviewers and editors are taught to think about theory in seminars can guide how you approach theory in your own work.

To gain more insight into that process, I searched <a href="https://www.opensyllabus.org/">opensyllabus.org</a> to find the theory-building papers that are assigned most frequently in graduate business seminars.[^1] I found that the distribution of theory papers follows a power law. A few classic papers appear in many courses. Many other papers only appear a few times. This suggests that a small number of papers shape how business researchers are taught to think about "theory" in grad school.

<script src="https://d3js.org/d3.v7.min.js"></script>
<style>

    .quote-box {
        max-width: 600px; /* Adjust width */
        margin: 40px auto; /* Centers the box */
        padding: 20px;
        border-left: 5px solid #6A41A1; /* Purple accent line */
        background: #f9f9f9;
        text-align: center;
        font-size: 1em;
        font-style: italic;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    .quote-box footer {
        margin-top: 10px;
        font-size: 0.9em;
        font-style: normal;
        color: #555;
    }


    .chart-container {
        display: flex;
        justify-content: center; /* Centers horizontally */
        align-items: center; /* Centers vertically */
        width: 100%; /* Full width */
        height: 300px; /* Full height */
    }

    svg {
        display: block;
        margin: auto;
    }

    .bar {
        fill: "red"; /*# "#6ab51a3"; */
    }

    .bar:hover {
        fill: #3f007d;
    }

    .axis-label {
        font-size: 12px;
        font-family: 'Roboto';
    }

    .x-axis path,
    .y-axis path {
        display: none;
    }

    /* Tooltip styles */
    .tooltip {
        position: absolute;
        text-align: center;
        padding: 8px;
        background-color: white;
        color: black;
        border: 1px solid black;
        border-radius: 5px;
        visibility: hidden;
        font-size: 14px;
        font-family: 'Roboto';
    }

    /* Default: Show titles */
    .y-axis-titles text {
        display: block;
    }

    /* On small screens (like mobile), hide titles */
    @media (max-width: 600px) {
        .y-axis-titles text {
            display: none;
        }
    }

</style>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">


<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 8px; /* Adds spacing inside cells */
        border: 1px solid #ddd; /* Adds a subtle border */
        text-align: left; /* Aligns text to the left */
    }

    th:first-child, td:first-child, 
    th:last-child, td:last-child {
        width: 25%; /* Adjust as needed */
        min-width: 200px; /* Ensures a minimum width */
    }

    th:nth-child(2), td:nth-child(2) {
        width: 50%; /* Middle column takes the most space */
    }

    ul {
        margin: 0;
        padding-left: 10px; /* Adjusts bullet indentation */
        list-style-position: inside; /* Moves bullet closer to the text */
    }
</style>


<div class="chart-container"></div>
<div id="tooltip" class="tooltip"></div>

<script>
      const jsonData = [
                      {
                          "Rank":1,
                          "Title":"What Constitutes a Theoretical Contribution?",
                          "Authors":"David A. Whetten",
                          "Publisher":"Academy of Management Review",
                          "Appearances":153,
                          "Score":14
                      },
                      {
                          "Rank":2,
                          "Title":"Building Theory About Theory Building",
                          "Authors":"Kevin G. Corley, Dennis A. Gioia",
                          "Publisher":"Academy of Management Review",
                          "Appearances":87,
                          "Score":8
                      },
                      {
                          "Rank":2,
                          "Title":"Theory Building From Cases",
                          "Authors":"Kathleen M. Eisenhardt, Melissa E. Graebner",
                          "Publisher":"Academy of Management Journal",
                          "Appearances":82,
                          "Score":8
                      },
                      {
                          "Rank":3,
                          "Title":"Trends in Theory Building and Theory Testing",
                          "Authors":"Jason A. Colquitt, Cindy P. Zapata-Phelan",
                          "Publisher":"Academy of Management Journal",
                          "Appearances":62,
                          "Score":6
                      },
                      {
                          "Rank":1,
                          "Title":"Theory Construction as Disciplined Imagination",
                          "Authors":"Karl E. Weick",
                          "Publisher":"Academy of Management Review",
                          "Appearances":49,
                          "Score":5
                      },
                      {
                          "Rank":4,
                          "Title":"Multiparadigm Perspectives on Theory Building",
                          "Authors":"Dennis A. Gioia, Evelyn Pitre",
                          "Publisher":"Academy of Management Review",
                          "Appearances":30,
                          "Score":3
                      },
                      {
                          "Rank":5,
                          "Title":"From Borrowing to Blending",
                          "Authors":"Cliff Oswick, Peter Fleming, Gerard Hanlon",
                          "Publisher":"Academy of Management Review",
                          "Appearances":25,
                          "Score":2
                      },
                      {
                          "Rank":6,
                          "Title":"Typologies as a Unique Form of Theory Building",
                          "Authors":"D. Harold Doty, William H. Glick",
                          "Publisher":"Academy of Management Review",
                          "Appearances":20,
                          "Score":2
                      },
                      {
                          "Rank":7,
                          "Title":"Theory Building",
                          "Authors":"Dean A. Shepherd, Roy Suddaby",
                          "Publisher":"Journal of Management",
                          "Appearances":19,
                          "Score":2
                      },
                      {
                          "Rank":9,
                          "Title":"A Definition of Theory",
                          "Authors":"John G. Wacker",
                          "Publisher":"Journal of Operations Management",
                          "Appearances":13,
                          "Score":1
                      },
                      {
                          "Rank":10,
                          "Title":"The Case for Inductive Theory Building",
                          "Authors":"Edwin A. Locke",
                          "Publisher":"Journal of Management",
                          "Appearances":12,
                          "Score":2
                      },
                      {
                          "Rank":13,
                          "Title":"Case Study Research Methods for Theory Building",
                          "Authors":"Arch G. Woodside, Elizabeth J. Wilson",
                          "Publisher":"Journal of Business & Industrial Marketing",
                          "Appearances":11,
                          "Score":1
                      },
                      {
                          "Rank":11,
                          "Title":"Theory Building and Cheap Talk About Legitimation",
                          "Authors":"Michael T. Hannan, Glenn R. Carroll",
                          "Publisher":"American Sociological Review",
                          "Appearances":11,
                          "Score":1
                      },
                      {
                          "Rank":12,
                          "Title":"Theory Building in Qualitative Research and Comput...",
                          "Authors":"Udo Kelle",
                          "Publisher":"Sociological Research Online",
                          "Appearances":11,
                          "Score":1
                      },
                      {
                          "Rank":14,
                          "Title":"Multilevel Theory Building",
                          "Authors":"Katherine J. Klein, Henry L. Tosi, Albert A. Cannella",
                          "Publisher":"Academy of Management Review",
                          "Appearances":10,
                          "Score":1
                      }
                  ];

        // Log JSON data
        console.log("JSON Data:", jsonData);

        const isMobile = window.innerWidth <= 600;
        const titleSpace = isMobile ? 20 : 250;
        const margin = {
            top: 20,
            right: 20,
            bottom: 40,
            left: titleSpace, // Space for titles
        };

        const barOffset = 5; // Bars start right after axis

        const container = d3.select(".chart-container");
        const containerWidth = container.node().getBoundingClientRect().width;
        const width = containerWidth - margin.left - margin.right;
        const height = 300 - margin.top - margin.bottom;

        const tooltip = d3.select("#tooltip");

        // Set up scales
        const x = d3.scaleLinear()
            .domain([0, d3.max(jsonData, d => d.Appearances)])
            .range([0, width]);

        const y = d3.scaleBand()
            .domain(jsonData.map(d => d.Title))
            .range([0, height])
            .padding(0.1);

        // Create SVG with viewBox for responsiveness
        const svg = container.append("svg")
            .attr("viewBox", `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .classed("svg-content", true)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // Draw bars
        svg.selectAll(".bar")
            .data(jsonData)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("y", d => y(d.Title))
            .attr("height", y.bandwidth())
            .attr("x", barOffset) // Bars start at 0 after axis
            .attr("width", d => x(d.Appearances))
            .attr("fill", "#6A41A1")
            .on("mouseover", function (event, d) {
                tooltip.style("opacity", 1).style("visibility", "visible")
                    .html(`<strong>${d.Title}</strong><br>Author: ${d.Authors}<br>Appearances: ${d.Appearances}`)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 28) + "px");
            })
            .on("mousemove", function (event) {
                tooltip.style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 28) + "px");
            })
            .on("mouseout", function () {
                tooltip.style("opacity", 0);
            });

        // Add X-axis
        svg.append("g")
            .attr("class", "x-axis")
            .attr("transform", `translate(0, ${height})`)
            .call(d3.axisBottom(x).ticks(5).tickSizeOuter(0));

        // Add Y-axis (titles hidden on mobile via CSS)
        svg.append("g")
            .attr("class", "y-axis y-axis-titles")
            .call(d3.axisLeft(y)
                .tickSize(0)) // Remove tick marks
            .selectAll("text")
            .attr("text-anchor", "end") // ✅ Right-justify the text
            .attr("dx", "-0.2em") // ✅ Shift text slightly closer to the bars
            .attr("dy", "0.35em"); // Center text vertically


        const divider = isMobile ? 2.5 : 3;
        console.log(divider)

        svg.append("text")
            .attr("x", (width + margin.left + margin.right) / divider) 
            .attr("y", -10)
            .attr("text-anchor", "middle")
            .style("font-size", "14px")
            .style("font-weight", "bold")
            .style("font-family", "'Roboto', sans-serif")
            .text("Theory Building Papers by Frequency");

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 5)
            .attr("text-anchor", "middle")
            .style("font-size", "14px")
            .style("font-family", "'Roboto', sans-serif")
            .text("Number of Appearances");
    </script>


To build my own understanding, I collected definitions of theory from frequently-assigned papers to create the table below. (<a href="https://journals.sagepub.com/doi/10.1177/1094428115624965">This</a> paper suggests making such tables to clarify constructs.)

From this process, I was surprised to find that many authors loosely followed Whetten (1989), who conceived of theory as an answer to (1) what constructs explain an empirical phenomenon, (2) how are those constructs related, and (3) why we should expect that such constructs explain the world. Wacker (1998) expresses the Whetten definition more concisely.

<div class="quote-box">
    <p>Theory is: "(1) definitions of terms or variables, (2) a domain where the theory applies, (3) a set of relationships of variables, and (4) specific predictions."</p>
    <footer>— Wacker (1998)</footer>
</div>


For me, this degree of consensus was somewhat unexpected. As others have  <a href="https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Doctoral_Resources/Sutton_Staw_What%20theory%20is%20not.pdf">noted</a>, it sometimes feels like every business school researcher thinks of "theory" in a slightly different way.

Nevertheless, there was still some variation among frequently-assigned theory papers. Weick (1989) described theorizing by drawing an analogy with natural selection, Gioia and Pitre (1990) argued for new conceptions of theory which better reflect research the diversity of business research (e.g., interpretivism), while Doty and Glick (1994) argued for building theory through organizational typology.

Yet despite this diversity, I think these papers offer a collective definition of theory that is both pretty consistent and pretty clear. Theory concisely asserts falsifiable, generalizable, and comprehensible empirical relationships among constructs.

The full table is shown below.


<table>
    <tr>
        <th>Author</th>
        <th>Definition of Theory</th>
        <th>Key Attributes</th>
    </tr>
    <tr>
        <td><strong><a href="https://www.jstor.org/stable/258554">Whetten (1989)</a></strong></td>
        <td>
          <ul style="
              list-style: none; 
              padding-left: 2em; 
              text-indent: -2em; 
              max-width: 600px; 
              word-break: break-word; 
              overflow-wrap: break-word;">
              <li>&nbsp;&nbsp;&nbsp;<strong>What:</strong> Which factors (variables, constructs, concepts) logically should be considered as part of the explanation of the social or individual phenomena of interest?</li>
              <li>&nbsp;&nbsp;&nbsp;<strong>How:</strong> Having identified a set of factors, the researcher's next question is how they are related? Operationally, this involves using 'arrows' to connect the 'boxes.'</li>
              <li>&nbsp;&nbsp;&nbsp;<strong>Why:</strong> What are the underlying psychological, economic, or social dynamics that justify the selection of factors and the proposed causal relationships?</li>
          </ul>
        </td>
        <td>
            <ul>
                <li>Offers a canonical definition of theory, which emphasizes networks of empirical relationships between constructs</li>
                <li>Can be <a href="https://www.abehandler.com/blog/2025/MISQ-theory/">expressed</a> as a Directed Acyclic Graph (DAG)</li>
                <li>Paper has been cited more than six thousand times; appears on over 100 syllabi</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://psycnet.apa.org/record/2011-00177-002">Corley & Gioia (2011)</a></strong></td>
        <td>
            "Theory is a statement of concepts and their interrelationships that shows how and/or why a phenomenon occurs."<br><br>
            "Our synthesis reveals two dimensions—originality and utility—that currently dominate considerations of theoretical contribution."
        </td>
        <td>
            <ul>
            <li> Breaks down theoretical contributions in terms of two axes: (A) originality and (B) utility</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://josephmahoney.web.illinois.edu/BADM504_Fall%202019/Eisenhardt%20and%20Graebner%20(2007).pdf">Eisenhardt & Graebner (2007)</a></strong></td>
        <td>
            "Theory-building research using cases typically answers research questions that address 'how' and 'why' in unexplored areas."<br><br>
            "When the research is done well, the propositions will be consistent with most (or even all) of the cases because the researcher has effectively 'pattern matched' between theory and data. It is also crucial to write the underlying theoretical arguments that provide the logical link between the constructs within a proposition."
        </td>
        <td>
            <ul>
                <li>Emphasizes inductive theory-building from multiple qualitative case studies</li>
                <li>Emphasizes connections between top-down deductive theory testing and bottom-up inductive theory building</li>
                <li>Emphasizes role of generalizability</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://psycnet.apa.org/record/2008-01202-003">Colquitt & Zapata-Phelan (2007)</a></strong></td>
        <td>
            "Many scholars define theory in terms of relationships between independent and dependent variables. For example, Campbell defined theory as 'a collection of assertions, both verbal and symbolic, that identifies what variables are important and for what reasons, specifies how they are interrelated and why, and identifies the conditions under which they should be related or not related.'"<br><br>
            "Theory allows scientists to understand and predict outcomes of interest."<br><br>
            "Theory also allows scientists to describe and explain a process or sequence of events."
        </td>
        <td>
            <ul>
                <li>Breaks down theoretical contributions in terms of two axes: theory building and theory testing</li>
                <li>Theory building describes different ways of adding to the network of constructs that explain a phenomenon (e.g., considering a new dependent variable or mediator)</li>
                <li>Theory testing describes checking existing theory against empirical data</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://www.jstor.org/stable/258556">Weick (1989)</a></strong></td>
        <td>
            "When theorists build theory, they design, conduct, and interpret imaginary experiments. In doing so, their activities resemble the three processes of evolution: variation, selection, and retention."<br><br>
            "The selection criteria by which a conjecture is selected or rejected include judgments of whether it is interesting, plausible, consistent, or appropriate."
        </td>
        <td>
            <ul>
                <li>Conceives of theory building as a process of thinking up explanations and then selecting good ones, similar to natural selection</li>
                <li>Attempts to decouple the process of thinking up theories from the process of testing them</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://psycnet.apa.org/record/1991-08556-001">Gioia & Pitre (1990)</a></strong></td>
        <td>
            "We broadly define theory as any coherent description or explanation of observed or experienced phenomena. This atypically broad definition is necessary to encompass the wide scope of theoretical representations found in the alternative paradigms."
        </td>
        <td>
            <ul>
                <li>Argues that traditional theory building in management is poorly suited to alternative research paradigms like interpretivism and radical humanism</li>
                <li>Calls for a multiparadigm perspective on theory construction that can accommodate different conceptions of theory</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://www.jstor.org/stable/pdf/41318003.pdf">Oswick, Fleming, & Hanlon (2011)</a></strong></td>
        <td>
            "For us, and in keeping with Bourdieu (1977), the term theory, in a broad sense, means 'a system of ideas or statements explaining something.'"<br><br>
            "We formulate theory through a generative engagement with other theories, concepts, constructs, and ideas that involve the use of various types of analogy and metaphor."
        </td>
        <td>
            <ul>
                <li>Describes how business research often borrows theory from outside disciplines like psychology, sociology, and economics</li>
                <li>Argues that borrowing constrains business research</li>
                <li>Advocates for a process of exchange between organizational research and reference disciplines</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://www.jstor.org/stable/258704">Doty & Glick (1994)</a></strong></td>
        <td>
            "A theory … is a series of logical arguments that specifies a set of relationships among concepts, constructs, or variables."<br><br>
            "Although there are no concise, unanimously accepted definitions of a theory, theory-building experts seem to agree that there are at least three primary criteria that theories must meet: (a) constructs must be identified, (b) relationships among these constructs must be specified, and (c) these relationships must be falsifiable."
        </td>
        <td>
            <ul>
                <li>Argues that organizational typologies can be theories because they:</li>
                <ul>
                    <li>Are distinct from classification systems</li>
                    <li>Meet traditional criteria for theory</li>
                    <li>Incorporate multiple levels of theory (p. 232)</li>
                </ul>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://onlinelibrary.wiley.com/doi/abs/10.1016/S0272-6963(98)00019-9">Wacker (1998)</a></strong></td>
        <td>
            "Generally, academics point to a theory as being made up of four components: definitions of terms or variables, a domain where the theory applies, a set of relationships of variables, and specific predictions."<br><br>
            "A clear explanation of how and why specific relationships lead to specific events."
        </td>
        <td>
            <ul>
                <li>Lists criteria for "good" theory such as uniqueness, internal consistency, and abstraction</li>
                <li>Repeats many of the same questions as Whetten (1989): Who, What, When, Where?</li>
            </ul>
        </td>
    </tr>
    <tr>
      <td><strong><a href="https://journals.sagepub.com/doi/10.1177/0149206307307636">Locke (2007)</a></strong></td>
      <td>
        "Instead of demanding a theory to start with, the introduction to a research paper could summarize what is known about the phenomenon in question and state the purpose of the proposed study: how it will go beyond what is known. Hypotheses would not be necessary; the author could simply pose questions."
      </td>
        <td>
            <ul>
                <li>Argues for inductive theory building, rather than deductive hypothesis testing</li>
                <li>Traces the philosophical roots of the traditional deductive approach</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://www.jstor.org/stable/259080">Klein, Tosi, and Cannella (1999)</a></strong></td>
        <td>
            "Multilevel theories span the levels of organizational behavior and performance, typically describing some combination of individuals, dyads, teams, businesses, corporations, and industries. Multilevel theories, thus, begin to bridge the micro-macro divide, integrating the micro domain's focus on individuals and groups with the macro domain's focus on organizations, environment, and strategy."
        </td>
        <td>
            <ul>
                <li>Describes multi-level theories which describe organizational phenomena at multiple levels of analysis (e.g., individual vs. firm vs. sector).</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong><a href="https://journals.sagepub.com/doi/full/10.1177/0149206316647102">Shepherd and Suddaby (2017)</a></strong></td>
        <td>
            "compelling theories are at their core compelling stories … Compelling stories are built around main characters who engage in a struggle with a powerful entity (narrative conflict) within a narrative setting"<br><br>
            "Rationalists see knowledge as most valuable when it is abstracted into general principles and relationships—namely, theory"
        </td>
        <td>
            <ul>
                <li>Argues that theory can be considered a form of storytelling with characters, tensions, and narrative arcs</li>
            </ul>
        </td>
    </tr>
</table>


### Data collection details

To create this post, I searched opensyllabus.org for paper titles included in business school syllabi. I used the queries "theoretical contribution," "theory building," and "theory construction" to discover three sets of paper titles, along with the number of syllabi appearances for each title. The <a href="https://gist.github.com/AbeHandler/f4dd1593190f592b894f2e7ed22c94d5">dataset</a> contains the union of all such search results. I limited each search to business syllabi. The table lists all papers included in at least 10 syllabi, with a few exceptions. I excluded Kelle (1997), Hannan and Carroll (1995), and Woodside and Wilson (2003) because these three articles did not focus directly on theory building (e.g., Kelle discusses software in qualitative research). The table is already pretty long.

[^1]: Open-syllabus does not actually allow you to search by graduate-level courses only. I am assuming that these papers appear in graduate syllabi, which seems reasonable. These papers focus on business research methods, and would not likely be assigned to undergrads.

