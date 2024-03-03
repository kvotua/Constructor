import { Awards } from "src/pages/Awards/Awards";
import { Edit } from "src/pages/Edit/Edit";
import Following from "src/pages/Gallery/Following";
import New from "src/pages/Gallery/New";
import Personal from "src/pages/Gallery/Personal";
import Popular from "src/pages/Gallery/Popular";
import { Home } from "src/pages/Home/Home";
import { Info } from "src/pages/Info/Info";
import { Profile } from "src/pages/Profile/Profile";
import { ProfileSettings } from "src/pages/ProfileSettings/ProfileSettings";
import { Quests } from "src/pages/Quests/Quests";
import { RoutesList } from "../types/routes/types";
import { AddProject } from "src/pages/AddProject/AddProject";
import { UserPage } from "src/pages/UserPage/UserPage";

export const appRoutes = [
  {
    path: RoutesList.Home,
    Component: Home,
  },
  {
    path: RoutesList.Info,
    Component: Info,
  },
];

export const projectRoutes = [
  {
    path: RoutesList.ProjectAdd,
    Component: AddProject,
  },
  {
    path: RoutesList.Project,
    Component: UserPage,
  },
  {
    path: RoutesList.ProjectEdit,
    Component: Edit,
  },
];

export const profileRoutes = [
  {
    path: RoutesList.Profile,
    Component: Profile,
  },
  {
    path: "/profile/awards/",
    Component: Awards,
  },
  {
    path: "/profile/quests/",
    Component: Quests,
  },
  {
    path: "/profile/settings/",
    Component: ProfileSettings,
  },
];

export const galleryRoutes = [
  {
    path: RoutesList.Gallery,
    Component: Popular,
  },
  {
    path: "/gallery/following/",
    Component: Following,
  },
  {
    path: "/gallery/new/",
    Component: New,
  },
  {
    path: "/gallery/personal/",
    Component: Personal,
  },
];
