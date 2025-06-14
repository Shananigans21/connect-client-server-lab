document.addEventListener("DOMContentLoaded", () => {
    fetch("/events")
      .then(res => res.json())
      .then(data => {
        data.forEach(renderEvent);
      });
  
    document.getElementById("event-form").addEventListener("submit", e => {
      e.preventDefault();
      const title = document.getElementById("title").value;
  
      fetch("/events", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title })
      })
      .then(res => res.json())
      .then(renderEvent);
  
      e.target.reset();
    });
  });
  
  function renderEvent(event) {
    const li = document.createElement("li");
    li.textContent = `${event.id}: ${event.title}`;
    document.getElementById("event-list").appendChild(li);
  }
  