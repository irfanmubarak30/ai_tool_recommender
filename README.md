# AI Tool Recommender 🤖

An intelligent AI-powered system that analyzes your tasks and recommends the most suitable AI tools and services. Built with CrewAI framework, this tool uses specialized AI agents to understand your requirements and provide tailored recommendations.

## 🚀 Features

- **Task Analysis**: Automatically analyzes your task requirements and determines needed AI capabilities
- **Comprehensive Research**: Searches across all major AI platforms and tools
- **Smart Recommendations**: Provides detailed recommendations with cost analysis and implementation guidance
- **Multi-Agent System**: Uses specialized AI agents for different aspects of the recommendation process

## 🏗️ Architecture

The system consists of three specialized AI agents:

### 1. Task Analyzer Agent
- **Role**: AI Task Requirements Engineer
- **Function**: Analyzes input tasks to determine required AI capabilities
- **Output**: JSON with task type, complexity, budget requirements, and specifications

### 2. AI Researcher Agent  
- **Role**: AI Tools Market Analyst
- **Function**: Researches and compares AI tools across different categories
- **Coverage**: OpenAI, Anthropic, Google, Microsoft, Stability AI, Hugging Face, and more

### 3. Recommender Agent
- **Role**: AI Solution Architect
- **Function**: Synthesizes research to provide optimal tool recommendations
- **Output**: Detailed recommendation report with justification

## 🔧 AI Tool Categories Covered

- **Text Generation**: OpenAI GPT, Claude, Gemini, local models
- **Image Generation**: DALL-E, Midjourney, Stable Diffusion
- **Audio Processing**: Whisper, ElevenLabs, speech synthesis
- **Video Generation**: RunwayML, Pika, video AI tools
- **Code Generation**: GitHub Copilot, CodeT5, programming assistants
- **Multimodal**: GPT-4V, Gemini Vision, multi-capability models
- **Data Processing**: Analytics and ML platforms

## 📋 Prerequisites

- Python 3.8+
- UV package manager (modern Python package manager)
- API keys for AI services (optional, based on usage)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/irfanmubarak30/ai_tool_recommender.git
   cd ai_tool_recommender
   ```

2. **Install UV (if not already installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # or on Windows:
   # powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Install dependencies using UV**
   ```bash
   uv sync
   ```

4. **Set up environment variables** (if needed)
   ```bash
   # Create a .env file for API keys
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

## 🚀 Usage

### Basic Usage

Run the main script using UV and enter your task description when prompted:

```bash
uv run main.py
```

Or activate the virtual environment first:
```bash
uv shell
python main.py
```

### Example Input/Output

**Input:**
```
Enter the task description: I need to create a chatbot for customer support that can handle text and voice interactions
```

**Output:**
The system will generate a detailed report (`report.md`) containing:
- Task analysis with complexity assessment
- Recommended AI tools and services
- Cost breakdown and comparison
- Implementation approach
- Alternative options and considerations

## 📊 Output Format

The system generates structured outputs:

### Task Analysis (JSON)
```json
{
  "task_type": "multimodal",
  "complexity_level": 4,
  "real_time_needed": true,
  "budget_range": "medium",
  "integration_complexity": "moderate",
  "specific_requirements": ["speech-to-text", "natural language processing", "voice synthesis"]
}
```

### Final Report (Markdown)
- Executive summary
- Detailed tool recommendations
- Pricing comparison
- Implementation roadmap
- Risk assessment

## 🗂️ File Structure

```
ai_tool_recommender/
├── main.py                 # Entry point
├── crew.py                 # CrewAI configuration
├── agents.yaml             # Agent definitions
├── tasks.yaml              # Task definitions
├── pyproject.toml          # Project dependencies and config
├── uv.lock                 # Dependency lock file
├── report.md               # Generated recommendations
└── README.md               # This file
```

## ⚙️ Configuration

### Customizing Agents

Edit `agents.yaml` to modify agent roles and capabilities:

```yaml
task_analyzer:
  role: "AI Task Requirements Engineer"
  goal: "Identify what type of AI capabilities are needed"
  backstory: "Expert at analyzing tasks..."
```

### Customizing Tasks

Edit `tasks.yaml` to modify task workflows:

```yaml
analyze_task:
  description: "Analyze this task and determine requirements..."
  expected_output: "JSON format requirements"
```

## 🎯 Use Cases

- **Developers**: Find the right AI APIs for your application
- **Businesses**: Choose AI tools for specific business processes
- **Researchers**: Compare AI capabilities for research projects
- **Students**: Learn about available AI tools and their applications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: https://github.com/irfanmubarak30/ai_tool_recommender
- **Issues**: https://github.com/irfanmubarak30/ai_tool_recommender/issues
- **CrewAI Documentation**: https://docs.crewai.com/

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the CrewAI documentation
- Review the example outputs in the repository

## 🏆 Acknowledgments

- Built with [CrewAI](https://crewai.com/) framework
- Inspired by the need for better AI tool selection
- Thanks to the AI community for continuous innovation

---

**Made with ❤️ by [Irfan Mubarak](https://github.com/irfanmubarak30)**
