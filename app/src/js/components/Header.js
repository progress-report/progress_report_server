import { Link } from 'react-router-dom';

const Header = () => (
  <header>
    <Link to="/" className="title"><b>ProgressReport</b></Link>
    <Link to="/report">Report</Link>
  </header>
);

export default Header;
