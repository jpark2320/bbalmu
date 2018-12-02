import * as React from "react";
import SummaryBoard from "./presenter";

interface IProps {
  title: string;
  region: string;
  category: string;
  summaryPosts: any;
  getSummaryPosts: () => object;
}

class Container extends React.Component<IProps> {
  public state = {
    page: 1
  };

  public componentDidMount() {
    const { getSummaryPosts, summaryPosts } = this.props;

    if (!summaryPosts) {
      getSummaryPosts();
    }
  }

  public render() {
    const { title, summaryPosts } = this.props;

    return <SummaryBoard title={title} summaryPosts={summaryPosts} />;
  }
}

export default Container;
