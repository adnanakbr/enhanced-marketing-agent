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
   
   **Step 4a: Authenticate with Google Cloud**
   ```bash
   # Authenticate with Google Cloud (opens browser for login)
   gcloud auth login
   
   # Verify authentication
   gcloud auth list
   ```
   
   **Step 4b: Set your project**
   ```bash
   # Replace YOUR_PROJECT_ID with your actual project ID
   gcloud config set project YOUR_PROJECT_ID
   
   # Verify project is set correctly
   gcloud config get-value project
   ```
   
   **Step 4c: Enable required APIs**
   ```bash
   # Enable Vertex AI API (for image generation)
   gcloud services enable aiplatform.googleapis.com
   
   # Enable Generative Language API (for text generation)
   gcloud services enable generativelanguage.googleapis.com
   
   # Verify APIs are enabled
   gcloud services list --enabled --filter="name:aiplatform OR name:generativelanguage"
   ```
   
   **Step 4d: Set up Application Default Credentials**
   ```bash
   # Set up application default credentials
   gcloud auth application-default login
   ```

5. **Configure environment variables**
   
   Create a `.env` file in the project root directory:
   ```bash
   # Create the .env file
   touch .env
   ```
   
   Add the following content to your `.env` file:
   ```bash
   # Google Cloud Configuration
   GOOGLE_CLOUD_PROJECT=your-actual-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```
   
   **Important Notes:**
   - Replace `your-actual-project-id` with your actual Google Cloud Project ID
   - You can find your Project ID in the Google Cloud Console dashboard
   - Common locations include: `us-central1`, `us-east1`, `europe-west1`, `asia-southeast1`
   - The `.env` file is already included in `.gitignore` to keep your credentials secure
   
   **Example .env file:**
   ```bash
   GOOGLE_CLOUD_PROJECT=my-marketing-agency-project-123
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

## 🔧 Troubleshooting

### Common Issues and Solutions

**Issue: "ModuleNotFoundError: No module named 'google'"**
```bash
# Solution: Make sure you're in the poetry environment
poetry shell
poetry install
```

**Issue: "Authentication failed" or "Permission denied"**
```bash
# Solution: Re-authenticate with Google Cloud
gcloud auth login
gcloud auth application-default login
```

**Issue: "Project not found" or "API not enabled"**
```bash
# Solution: Verify your project and enable APIs
gcloud config get-value project
gcloud services enable aiplatform.googleapis.com
gcloud services enable generativelanguage.googleapis.com
```

**Issue: "Environment variables not found"**
```bash
# Solution: Check your .env file exists and has correct values
ls -la .env
cat .env
```

**Issue: "Image generation failed"**
- Ensure Vertex AI API is enabled
- Check that your project has billing enabled
- Verify the location in your .env file matches your project's region

**Issue: "Poetry command not found"**
```bash
# Solution: Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
# Or on macOS with Homebrew:
brew install poetry
```

### Getting Help

If you encounter issues not covered here:
1. Check the [GitHub Issues](https://github.com/adnanakbr/enhanced-marketing-agent/issues) page
2. Create a new issue with:
   - Your operating system
   - Python version (`python3 --version`)
   - Error message (full traceback)
   - Steps you've already tried

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