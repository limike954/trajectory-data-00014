/* eslint-env node */
import { Footer, Layout, Navbar } from "nextra-theme-docs";
import { Head } from "nextra/components";
import { getPageMap } from "nextra/page-map";
import { Providers } from "./components/Providers";
import "nextra-theme-docs/style.css";

export const metadata = {
  metadataBase: new URL("https://github.com/limike954/trajectory-data-00014"),
  title: {
    template: "%s - Alith",
  },
  description: "Alith: Web3 Friendly AI Agents for Everyone",
  applicationName: "Alith",
  generator: "Next.js",
  appleWebApp: {
    title: "Nextra",
  },
  other: {
    "msapplication-TileImage": "/ms-icon-144x144.png",
    "msapplication-TileColor": "#fff",
  },
};

export default async function RootLayout({ children }) {
  const navbar = (
    <Navbar
      logo={
        <div>
          <b>Alith</b>{" "}
        </div>
      }
      projectLink="https://github.com/limike954/trajectory-data-00014"
    />
  );
  const footer = <Footer hidden={true} />;
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head faviconGlyph="✦" />
      <body>
        <Providers>
          <Layout
            navbar={navbar}
            footer={footer}
            editLink="Edit this page on GitHub"
            docsRepositoryBase="https://github.com/limike954/trajectory-data-00014/blob/main/website/src/content"
            sidebar={{ defaultMenuCollapseLevel: 1 }}
            pageMap={await getPageMap()}
          >
            {children}
          </Layout>
        </Providers>
      </body>
    </html>
  );
}
