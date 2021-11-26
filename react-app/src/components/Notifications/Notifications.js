import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useModal } from "../../context/UseModal";
import { getUserNotif } from "../../store/notification";
import { useHistory } from "react-router";
import "./Notifications.css";

const Notifications = () => {
  const dispatch = useDispatch();
  const { setNum } = useModal();
  const history = useHistory();
  const user = useSelector((state) => state.session.user);
  const notifications = useSelector(
    (state) => state.notification.notifications
  );

  useEffect(() => {
    dispatch(getUserNotif());
  }, [user]);

  const redirect = (e, id) => {
    e.stopPropagation();
    history.push(`/users/${id}`);
    setNum(0);
  };

  return (
    <>
      {notifications?.length > 0
        ? notifications.slice(0, 5).map((n) => (
            <>
              {n.sender.id !== user?.id && (
                <div
                  key={n}
                  className="notif-card"
                  onClick={() => {
                    history.push(n.link);
                    setNum(0);
                  }}
                >
                  <img
                    onClick={(e) => redirect(e, n.sender.id)}
                    src={n.sender.image_url}
                    className="notif-img"
                  />
                  <div className="notif-sender">
                    <div className="notif-username">{n.sender.username}</div>
                    <div className="notif-msg">{n.message}</div>
                  </div>
                </div>
              )}
            </>
          ))
        : null}
    </>
  );
};

export default Notifications;
