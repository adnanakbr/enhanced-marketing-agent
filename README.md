# Enhanced Marketing Agency - AI-Powered Marketing Assistant

## 🚀 Overview

This AI-powered marketing agency assistant is designed to help businesses and individuals create comprehensive marketing materials based on their brand information. The agent can generate visualizations, social media content, web content, marketing briefs, and banners using advanced AI models including Gemini for text and image generation.

## ✨ Key Features

### 🎨 **Fancy Visualizations**
- Create compelling visual representations of brand strategies
- AI-generated images using Gemini image models
- Brand-aligned visual concepts for presentations and marketing materials

### 📱 **Social Media Content**
- Platform-specific posts for Twitter, Instagram, LinkedIn, Facebook
- Optimized character limits, hashtags, and calls-to-action
- Engagement strategies and posting recommendations

### 🌐 **Comprehensive Web Content**
- SEO-optimized landing pages, blog posts, product descriptions
- Brand-aligned messaging and conversion-focused copy
- Internal linking suggestions and performance optimization

### 📋 **Marketing Briefs**
- Strategic frameworks with actionable recommendations
- Target audience analysis and competitive positioning
- Implementation roadmaps and success metrics

### 🖼️ **Social Media Banners**
- Platform-optimized banners for all major social media platforms
- Brand-aligned design with professional quality
- Proper dimensions and specifications for each platform

### 🏢 **Traditional Marketing Services**
- Domain name suggestions and availability checking
- Professional website creation
- Marketing strategy development
- Logo design and branding

## 🛠️ Setup and Installation

### Prerequisites

- **Python 3.9+**
- **Poetry** (for dependency management)
- **Google Cloud Platform** project with Vertex AI enabled
- **Google Cloud CLI** installed and configured

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd marketing-agency
   ```

2. **Install Poetry** (if not already installed)
        ```bash
        pip install poetry
        ```

3. **Install dependencies**
    ```bash
    poetry install
    ```

4. **Set up Google Cloud credentials**
   ```bash
   # Authenticate with Google Cloud
   gcloud auth login
   
   # Set your project
   gcloud config set project YOUR_PROJECT_ID
   
   # Enable required APIs
   gcloud services enable aiplatform.googleapis.com
   gcloud services enable generativelanguage.googleapis.com
   ```

5. **Configure environment variables**
   Create a `.env` file in the project root:
        ```bash
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

6. **Activate the virtual environment**
```bash
   poetry shell
```

## 🚀 Usage

### Running the Agent

1. **Start the agent**
```bash
   poetry run python -m marketing_agency
   ```

2. **Interactive Mode**
   The agent will start in interactive mode where you can:
   - Provide brand information
   - Choose from available marketing services
   - Generate content and visualizations

### Example Usage

#### Brand-Based Workflow (Recommended)

```
User: "I have a sustainable fashion brand called EcoStyle. We focus on eco-friendly clothing for young professionals aged 25-35. Our values are sustainability, quality, and style. Can you help me create marketing materials?"

Agent: "I understand you have EcoStyle, a sustainable fashion brand targeting young professionals. I can help you create:
1. Fancy visualizations of your brand strategy
2. Social media posts for various platforms
3. Comprehensive web content
4. Marketing briefs
5. Social media banners

Which services would you like me to create for you?"
```

#### Service Selection Examples

**Visualizations:**
```
User: "I'd like a visualization of my brand strategy"
Agent: [Creates AI-generated image representing EcoStyle's sustainable fashion concept]
```

**Social Media Posts:**
```
User: "Create Twitter posts for my brand"
Agent: [Generates platform-optimized Twitter posts with hashtags and CTAs]
```

**Marketing Brief:**
```
User: "I need a comprehensive marketing brief"
Agent: [Creates detailed marketing brief with strategic framework and recommendations]
```

### Traditional Domain-Based Workflow

If you prefer the traditional approach:

```
User: "I want to start with domain selection"
Agent: [Guides through domain creation, website building, marketing strategy, and logo design]
```

## 🏗️ Architecture

### Agent Structure

```
marketing_coordinator (Main Agent)
├── visualization_create_agent
├── social_media_create_agent
├── web_content_create_agent
├── marketing_brief_create_agent
├── banner_create_agent
├── domain_create_agent
├── website_create_agent
├── marketing_create_agent
└── logo_create_agent
```

### Key Components

- **Main Coordinator**: Routes requests and manages workflow
- **Sub-Agents**: Specialized agents for specific marketing tasks
- **Image Generation**: Uses Gemini Imagen models for visual content
- **Text Generation**: Uses Gemini 2.5 Pro for content creation

## 📁 Project Structure

```
marketing-agency/
├── marketing_agency/
│   ├── __init__.py
│   ├── agent.py                 # Main coordinator agent
│   ├── prompt.py               # Main agent prompts
│   └── sub_agents/
│       ├── visualization_create/
│       ├── social_media_create/
│       ├── web_content_create/
│       ├── marketing_brief_create/
│       ├── banner_create/
│       ├── domain_create/
│       ├── website_create/
│       ├── marketing_create/
│       └── logo_create/
├── demo_html/                  # Demo website files
├── deployment/                 # Deployment scripts
├── eval/                      # Evaluation tools
├── tests/                     # Test files
├── pyproject.toml            # Project configuration
├── poetry.lock               # Dependency lock file
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID | Yes |
| `GOOGLE_CLOUD_LOCATION` | GCP region (e.g., us-central1) | Yes |

### Model Configuration

The agent uses the following models:
- **Text Generation**: `gemini-2.5-pro`
- **Image Generation**: `imagen-3.0-generate-002`

## 🧪 Testing

Run the test suite:

```bash
poetry run pytest tests/
```

## 🚀 Deployment

### Local Development

```bash
poetry run python -m marketing_agency
```

### Cloud Deployment

Use the deployment scripts in the `deployment/` directory:

```bash
cd deployment
python deploy.py
```

## 📊 Features Comparison

| Feature | Original | Enhanced |
|---------|----------|----------|
| Domain Selection | ✅ | ✅ |
| Website Creation | ✅ | ✅ |
| Marketing Strategy | ✅ | ✅ |
| Logo Design | ✅ | ✅ |
| Brand Visualizations | ❌ | ✅ |
| Social Media Content | ❌ | ✅ |
| Web Content Creation | ❌ | ✅ |
| Marketing Briefs | ❌ | ✅ |
| Social Media Banners | ❌ | ✅ |
| Brand-Based Workflow | ❌ | ✅ |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Google's Ads Development Kit (ADK)
- Powered by Gemini AI models
- Uses Vertex AI for image generation

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Check the documentation in the `docs/` directory
- Review the example usage in the `demo_html/` directory

## 🔄 Version History

- **v2.0.0** - Enhanced with 5 new marketing services and brand-based workflow
- **v1.0.0** - Initial release with domain-based marketing workflow

---

**Ready to revolutionize your marketing? Start by providing your brand information and let the AI create comprehensive marketing materials for you!** 🚀