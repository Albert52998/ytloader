import './App.css';
import HeadBan from './components/headban';
import Help from './components/Help';
// import DownloadComplete from './components/DownloadComplete';
// import DownloadFailed from './components/DownloadFailed';
import {Route, Switch} from 'react-router-dom';

function App() {
  return (
      <div className="App">
        <Switch>
          <Route path='/' exact component={HeadBan} />
          <Route path='/help/' exact component={Help} />
          {/*<Route path='/download-complete/' exact component={DownloadComplete} />*/}
          {/*<Route path='/download-failed/' exact component={DownloadFailed} />*/}
        </Switch>
      </div>
  );
}

export default App;
