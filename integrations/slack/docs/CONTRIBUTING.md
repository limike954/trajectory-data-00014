# 🤝 Contributing to LazAI Slack Bot

Thank you for your interest in contributing to the LazAI Slack Bot! This guide will help you get started with contributing code, documentation, and improvements.

## 🎯 How to Contribute

### Types of Contributions We Welcome

- 🐛 **Bug fixes** - Fix issues and improve stability
- ✨ **New features** - Add functionality that benefits users
- 📚 **Documentation** - Improve guides, API docs, and examples
- 🧪 **Tests** - Add test coverage and quality assurance
- 🎨 **UI/UX improvements** - Better user experience in Slack
- 🔧 **Performance optimizations** - Make the bot faster and more efficient

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/alith.git
cd alith/integrations/slack

# Add upstream remote
git remote add upstream https://github.com/limike954/trajectory-data-00014
```

### 2. Set Up Development Environment

```bash
# Install dependencies
npm install

# Copy environment template
cp .env.example .env
# Fill in your tokens and credentials

# Validate setup
npm run test:setup

# Start development mode
npm run dev
```

### 3. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-amazing-feature

# Or for bug fixes
git checkout -b fix/bug-description
```

## 📝 Development Guidelines

### Code Style

We use TypeScript with strict type checking. Follow these guidelines:

```typescript
// ✅ Good: Use proper typing
interface UserContribution {
  fileId: string;
  fileName: string;
  reward: number;
  timestamp: Date;
}

// ✅ Good: Use async/await
async function contributeFile(fileData: Buffer): Promise<ContributionResult> {
  try {
    const result = await processFile(fileData);
    return { success: true, ...result };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

// ✅ Good: Use meaningful names
const MAX_FILE_SIZE = 100 * 1024 * 1024; // 100MB
const SUPPORTED_EXTENSIONS = [".json", ".csv", ".txt"];

// ❌ Avoid: Any types without good reason
function processData(data: any): any {
  return data.whatever;
}
```

### File Organization

```
src/
├── commands/          # Slash command handlers
│   ├── contribute.ts  # /lazai-contribute logic
│   ├── balance.ts     # /lazai-balance logic
│   └── status.ts      # /lazai-status logic
├── services/          # Business logic
│   ├── fileService.ts # File handling
│   ├── lazaiService.ts# LazAI integration
│   └── slackService.ts# Slack API helpers
├── utils/             # Utility functions
├── types/             # TypeScript type definitions
└── config/            # Configuration management
```

### Error Handling

Always handle errors gracefully with user-friendly messages:

```typescript
// ✅ Good: Comprehensive error handling
try {
  const result = await uploadToIPFS(fileData);
  return { success: true, url: result.url };
} catch (error) {
  if (error.code === "FILE_TOO_LARGE") {
    return {
      success: false,
      error: "File exceeds 100MB limit",
      userMessage:
        "❌ Your file is too large. Please try a file smaller than 100MB.",
    };
  }

  console.error("IPFS upload failed:", error);
  return {
    success: false,
    error: error.message,
    userMessage: "❌ Upload failed. Please try again in a moment.",
  };
}
```

### Testing

Write tests for new functionality:

```typescript
// Example test structure
describe("File Contribution", () => {
  it("should accept valid JSON files", async () => {
    const mockFile = createMockFile("test.json", validJSONContent);
    const result = await contributeFile(mockFile);

    expect(result.success).toBe(true);
    expect(result.fileId).toBeDefined();
    expect(result.reward).toBeGreaterThan(0);
  });

  it("should reject oversized files", async () => {
    const largeFile = createMockFile("large.json", oversizedContent);
    const result = await contributeFile(largeFile);

    expect(result.success).toBe(false);
    expect(result.error).toContain("too large");
  });
});
```

## 🔄 Development Workflow

### 1. Before You Start

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create your feature branch
git checkout -b feature/your-feature
```

### 2. During Development

```bash
# Run in development mode
npm run dev

# Run tests frequently
npm test

# Validate code style
npm run lint

# Check types
npm run type-check
```

### 3. Testing Your Changes

```bash
# Validate complete setup
npm run validate

# Test specific functionality
npm run test:commands
npm run test:integration

# Manual testing in Slack
# 1. Start bot: npm run dev
# 2. Test commands in Slack workspace
# 3. Verify file contributions work
# 4. Check error scenarios
```

### 4. Before Submitting

```bash
# Ensure code is clean
npm run lint:fix
npm run format

# Run full test suite
npm run test:all

# Build successfully
npm run build

# Update documentation if needed
# Update CHANGELOG.md
```

## 📋 Pull Request Process

### 1. Create a Good PR Title

```
✨ feat: Add batch file contribution support
🐛 fix: Handle network timeouts gracefully
📚 docs: Add troubleshooting guide for IPFS issues
🧪 test: Add integration tests for file validation
🎨 style: Improve progress bar animations
```

### 2. PR Description Template

```markdown
## 🎯 What does this PR do?

Brief description of the changes and why they're needed.

## 🔧 Changes Made

- [ ] Added new feature X
- [ ] Fixed bug Y
- [ ] Updated documentation Z
- [ ] Added tests for W

## 🧪 Testing

- [ ] All existing tests pass
- [ ] Added new tests for new functionality
- [ ] Manually tested in Slack workspace
- [ ] Tested edge cases and error scenarios

## 📸 Screenshots (if applicable)

[Add screenshots of new UI elements or Slack interactions]

## 🔗 Related Issues

Fixes #123
Related to #456

## 📝 Additional Notes

Any additional context, breaking changes, or migration notes.
```

### 3. Review Process

1. **Automated checks** must pass (tests, linting, build)
2. **Code review** by maintainers
3. **Manual testing** of functionality
4. **Documentation** review if applicable
5. **Approval** and merge

## 🎨 Feature Ideas & Roadmap

### High Priority Features

- **Batch File Processing**: Upload multiple files at once
- **File Validation**: Pre-validate files before contribution
- **Analytics Dashboard**: Team contribution statistics
- **Notification Settings**: Customize alert preferences

### Medium Priority Features

- **Slack Workflows**: Integration with Slack's workflow builder
- **Custom Rewards**: Set different reward amounts per file type
- **Team Leaderboards**: Gamification for team contributions
- **File Categories**: Organize contributions by type/project

### Low Priority Features

- **Mobile App**: React Native companion app
- **Voice Commands**: Slack voice interaction support
- **AI Integration**: Smart file categorization
- **Cross-Platform**: Discord, Teams integrations

## 🐛 Bug Reports

When reporting bugs, please include:

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**

- OS: [e.g. Windows 10, macOS Big Sur]
- Node.js version: [e.g. 18.17.0]
- Bot version: [e.g. 1.0.0]
- Slack client: [e.g. Desktop app, Web browser]

**Additional context**
Console logs, error messages, etc.
```

## 📚 Documentation Guidelines

### Writing Style

- **Clear and concise** - Use simple language
- **Examples included** - Show don't just tell
- **Step-by-step** - Break complex tasks into steps
- **Troubleshooting** - Include common issues and solutions
- **Screenshots** - Visual guides for UI elements

### Documentation Types

- **README.md** - Overview and quick start
- **Setup guides** - Detailed installation instructions
- **API documentation** - Technical reference
- **User guides** - How to use features
- **Troubleshooting** - Common problems and solutions

## 🏆 Recognition

Contributors will be recognized in:

- **README.md** - Contributors section
- **Release notes** - Feature attribution
- **Community posts** - Social media shoutouts
- **LazAI Ambassador Program** - Special recognition for active contributors

## 📞 Getting Help

### Before You Ask

1. Check existing [GitHub issues](https://github.com/limike954/trajectory-data-00014/issues)
2. Read the documentation thoroughly
3. Search previous discussions

### How to Get Help

- **GitHub Discussions** - For general questions
- **GitHub Issues** - For bugs and feature requests
- **Discord** - Real-time community support
- **Email** - For private/security concerns

### Response Times

- **Bug reports** - Within 24 hours
- **Feature requests** - Within 48 hours
- **Questions** - Within 24 hours
- **Pull reviews** - Within 72 hours

## 📋 Checklist for Contributors

### Before Starting

- [ ] Read this contributing guide
- [ ] Set up development environment
- [ ] Join community Discord/Slack
- [ ] Understand the project goals

### During Development

- [ ] Follow code style guidelines
- [ ] Write tests for new features
- [ ] Update documentation
- [ ] Test manually in Slack

### Before Submitting

- [ ] All tests pass
- [ ] Code is properly formatted
- [ ] Documentation is updated
- [ ] PR template is filled out

### After Submission

- [ ] Respond to review feedback
- [ ] Make requested changes
- [ ] Keep PR up to date with main branch

## 🎉 Thank You!

Every contribution helps make LazAI more accessible and powerful. Whether it's code, documentation, bug reports, or feature ideas - your input matters!

**Ready to contribute? Start by exploring the codebase and picking an issue labeled `good first issue`!** 🚀

---

_For questions about contributing, reach out to the maintainers or open a GitHub Discussion._
